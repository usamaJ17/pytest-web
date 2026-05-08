---
sidebar_position: 6
title: How It Works
---

# How It Works

pytest-web is a thin layer around standard pytest — it doesn't replace or patch pytest, it just orchestrates it.

---

## Architecture overview

```
Browser (UI)
    │  WebSocket (live events)
    │  HTTP (fetch/run/cancel)
    ▼
FastAPI server  ←──── HTTP webhook ────  pytest subprocess
(server.py)                               (plugin.py loaded)
    │
    └── spawns ──► pytest --collect-only   (Discover)
    └── spawns ──► pytest <nodeids> -n N   (Run)
```

---

## Step by step

### 1. Discover

When you click **Fetch Tests**, the server runs:

```bash
pytest --collect-only -q -p pytest_web.plugin
```

The plugin writes all collected node IDs to a temp JSON file. The server reads that file and returns the list to the browser. The browser renders one row per test, grouped by file.

The `-k` / `-m` args you type are passed straight to pytest's collector — so pytest's own filtering logic applies, including parametrize expansion.

### 2. Run

When you click **▶ Run Selected**, the server launches:

```bash
pytest <selected-nodeids> -n <workers> -p pytest_web.plugin
```

The plugin is injected via `-p pytest_web.plugin`. It reads two environment variables set by the server:

| Variable | Purpose |
|----------|---------|
| `PYTEST_WEB_WEBHOOK` | URL to POST events to |
| `PYTEST_WEB_RUN_ID` | UUID to correlate events with the current run |

### 3. Stream events

As tests run, the plugin fires HTTP POSTs to `POST /internal/event` on the FastAPI server:

| Event | When |
|-------|------|
| `session_start` | After collection, before the first test |
| `test_start` | When a test begins executing |
| `test_end` | When a test finishes (with outcome + duration) |
| `session_end` | When the entire run finishes |

`test_start` uses a **synchronous** HTTP call to guarantee it arrives before the first `test_end`. All other events are fire-and-forget (daemon thread) so they never block test execution.

### 4. Broadcast to browser

The server receives each event and broadcasts it over **WebSocket** to all connected browser tabs. The browser updates the test row's status dot and counters in real time.

On WebSocket connect (or reconnect), the server sends a **snapshot** of current run state — so a refreshed browser tab can rebuild the live view without missing anything.

### 5. xdist deduplication

When running with multiple workers, `pytest-xdist` re-fires each worker's report in the master process. Without deduplication, every test would be counted twice. pytest-web tracks `started` and `finished` node ID sets per run and silently drops duplicate events.

---

## Key design decisions

**No monkey-patching** — the plugin only uses standard pytest hooks (`pytest_sessionstart`, `pytest_collection_finish`, `pytest_runtest_logstart`, `pytest_runtest_logreport`, `pytest_sessionfinish`). Your test suite runs identically with or without the plugin.

**Safe to load anywhere** — the plugin is a no-op when `PYTEST_WEB_WEBHOOK` and `PYTEST_WEB_COLLECT_FILE` are absent. You can add `-p pytest_web.plugin` to your `addopts` permanently and it won't affect normal pytest runs.

**No build step** — the frontend is vanilla JS with no bundler. `static/app.js` is served directly. Frontend changes are visible on browser refresh with zero tooling.
