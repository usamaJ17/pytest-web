"""
Pytest plugin injected via -p pytest_web.plugin during /discover and /run.
Reads env vars set by the FastAPI server; all behaviour is a no-op when they
are absent so the plugin is safe to load in any pytest run.
"""

import json
import os
import queue
import threading
import time
import urllib.request

COLLECT_FILE = os.environ.get("PYTEST_WEB_COLLECT_FILE")
WEBHOOK = os.environ.get("PYTEST_WEB_WEBHOOK")
RUN_ID = os.environ.get("PYTEST_WEB_RUN_ID")

_session = None
_item_count: int = 0

_event_queue: queue.Queue = queue.Queue()
_worker_started = False
_worker_lock = threading.Lock()


def _worker_loop() -> None:
    while True:
        payload = _event_queue.get()
        try:
            if payload is None:
                return
            try:
                body = json.dumps({**payload, "run_id": RUN_ID}).encode()
                req = urllib.request.Request(
                    WEBHOOK, data=body, headers={"Content-Type": "application/json"}
                )
                urllib.request.urlopen(req, timeout=5.0)
            except Exception:
                pass  # never crash; UI tolerates missing events via WS snapshot
        finally:
            _event_queue.task_done()


def _ensure_worker() -> None:
    global _worker_started
    if _worker_started:
        return
    with _worker_lock:
        if _worker_started:
            return
        threading.Thread(
            target=_worker_loop, daemon=True, name="pytest-web-poster"
        ).start()
        _worker_started = True


def _post(payload: dict) -> None:
    """Enqueue an event for delivery. Never blocks pytest."""
    if not WEBHOOK:
        return
    _ensure_worker()
    _event_queue.put(payload)


def _is_xdist_worker() -> bool:
    """True if running inside an xdist worker process (vs. the master)."""
    return _session is not None and hasattr(_session.config, "workerinput")


# ── Collection hooks ──────────────────────────────────────────────


def pytest_sessionstart(session) -> None:
    global _session
    _session = session


def pytest_collection_finish() -> None:
    """
    Fires after ALL pytest_collection_modifyitems hooks have run (including
    pytest's own trylast -k / -m filters). Reading session.items here gives
    the final filtered list, so -k / -m args are correctly respected.
    """
    global _item_count
    if not _session:
        return

    if _is_xdist_worker():
        return

    items = list(_session.items)
    _item_count = len(items)

    if COLLECT_FILE:
        with open(COLLECT_FILE, "w") as f:
            json.dump([item.nodeid for item in items], f)

    # Synchronous POST — guarantees session_start arrives at the server
    # before any test_start (which is enqueued asynchronously below).
    if WEBHOOK:
        body = json.dumps(
            {"event": "session_start", "total": _item_count, "run_id": RUN_ID}
        ).encode()
        req = urllib.request.Request(
            WEBHOOK, data=body, headers={"Content-Type": "application/json"}
        )
        try:
            urllib.request.urlopen(req, timeout=5.0)
        except Exception:
            pass


# ── Run hooks ─────────────────────────────────────────────────────


def pytest_runtest_logstart(nodeid: str, location) -> None:
    _post({"event": "test_start", "nodeid": nodeid})


def pytest_runtest_logreport(report) -> None:
    if report.when == "call":
        _post(
            {
                "event": "test_end",
                "nodeid": report.nodeid,
                "outcome": report.outcome,
                "duration": round(report.duration, 4),
                "longrepr": str(report.longrepr) if report.failed else None,
            }
        )
    elif report.when == "setup":
        if report.skipped:
            # Skipped tests never reach the "call" phase.
            _post(
                {
                    "event": "test_end",
                    "nodeid": report.nodeid,
                    "outcome": "skipped",
                    "duration": 0.0,
                    "longrepr": None,
                }
            )
        elif report.failed:
            _post(
                {
                    "event": "test_end",
                    "nodeid": report.nodeid,
                    "outcome": "failed",
                    "duration": round(report.duration, 4),
                    "longrepr": str(report.longrepr),
                }
            )


def pytest_sessionfinish(session, exitstatus) -> None:
    _post({"event": "session_end", "exit_status": int(exitstatus)})
    if _worker_started:
        deadline = time.monotonic() + 10.0
        while time.monotonic() < deadline:
            if _event_queue.unfinished_tasks == 0:
                break
            time.sleep(0.05)