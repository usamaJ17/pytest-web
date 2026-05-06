import argparse
import os
import sys
import threading
import time
import webbrowser

from pytest_web import __version__

BANNER = r"""
                 __            __                     __
    ____  __  __/ /____  _____/ /_     _      _____  / /_
   / __ \/ / / / __/ _ \/ ___/ __/____| | /| / / _ \/ __ \
  / /_/ / /_/ / /_/  __(__  ) /_/_____/ |/ |/ /  __/ /_/ /
 / .___/\__, /\__/\___/____/\__/      |__/|__/\___/_.___/
/_/    /____/
"""


def _print_banner(url: str) -> None:
    use_color = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None
    if use_color:
        cyan = "\033[36m"
        dim = "\033[2m"
        reset = "\033[0m"
    else:
        cyan = dim = reset = ""
    sys.stdout.write(f"{cyan}{BANNER}{reset}")
    sys.stdout.write(
        f"  {dim}v{__version__}{reset}   {cyan}{url}{reset}   {dim}(Ctrl+C to stop){reset}\n\n"
    )
    sys.stdout.flush()


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="pytest-web",
        description="Local web UI for pytest — run from your project root",
    )
    parser.add_argument("--host", default="127.0.0.1", help="Bind host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Port (default: 8000)")
    parser.add_argument("--cwd", default=None, help="Project directory (default: current dir)")
    parser.add_argument(
        "--no-browser", action="store_true", help="Don't open browser automatically"
    )
    args = parser.parse_args()

    cwd = os.path.abspath(args.cwd or os.getcwd())
    if not os.path.isdir(cwd):
        print(f"error: directory not found: {cwd}", file=sys.stderr)
        sys.exit(1)

    os.environ["PYTEST_WEB_HOST"] = args.host
    os.environ["PYTEST_WEB_PORT"] = str(args.port)
    os.environ["PYTEST_WEB_CWD"] = cwd

    url = f"http://{args.host}:{args.port}"
    _print_banner(url)

    if not args.no_browser:

        def _open_browser():
            time.sleep(1.0)
            webbrowser.open(url)

        threading.Thread(target=_open_browser, daemon=True).start()

    try:
        import uvicorn

        uvicorn.run(
            "pytest_web.server:app",
            host=args.host,
            port=args.port,
            log_level="warning",
        )
    except KeyboardInterrupt:
        print("\n  Stopped.\n")
