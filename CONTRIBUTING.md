# Contributing to pytest-web

Thanks for your interest in contributing! This guide covers everything you need to go from zero to a merged PR.

## Table of contents

- [Getting started](#getting-started)
- [Development setup](#development-setup)
- [Running the app locally](#running-the-app-locally)
- [Linting and formatting](#linting-and-formatting)
- [Submitting a pull request](#submitting-a-pull-request)
- [Good first issues](#good-first-issues)
- [Project structure](#project-structure)

---

## Getting started

1. **Fork** the repo on GitHub, then clone your fork:
   ```bash
   git clone https://github.com/<your-username>/pytest-web.git
   cd pytest-web
   ```

2. Create a branch for your change:
   ```bash
   git checkout -b my-feature
   ```

## Development setup

You need Python 3.9+ and pip.

```bash
# Install the package in editable mode with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks (runs ruff on every commit)
pre-commit install
```

Verify the install:
```bash
python -c "import pytest_web; print(pytest_web.__version__)"
pytest-web --help
```

## Running the app locally

```bash
# From your own project directory (where tests live)
cd /path/to/your/project
pytest-web

# Or point it at a directory
pytest-web --cwd /path/to/your/project
```

The UI opens at `http://127.0.0.1:8000` automatically.

For frontend changes (`pytest_web/static/`), just refresh the browser — no build step required.

## Linting and formatting

We use [ruff](https://docs.astral.sh/ruff/) for both linting and formatting.

```bash
# Check for issues
ruff check .

# Auto-fix
ruff check --fix .

# Format
ruff format .
```

Pre-commit runs both automatically on `git commit`. CI will reject PRs that fail either check.

## Submitting a pull request

1. Make sure `ruff check .` and `ruff format --check .` pass locally.
2. Push your branch and open a PR against `main`.
3. Fill in the PR template — describe what changed and why.
4. A maintainer will review within a few days. Small, focused PRs get reviewed faster.

**PR tips:**
- One logical change per PR.
- If you're adding a feature, update the relevant section in `README.md`.
- If you're changing CLI behaviour, update the CLI flags table in `README.md`.

## Good first issues

Look for issues labeled [`good first issue`](https://github.com/usamaJ17/pytest-web/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) — these are scoped small and have clear acceptance criteria.

Not sure where to start? Feel free to open a Discussion or comment on any open issue.

## Project structure

```
pytest_web/
  cli.py        # Entry point — argument parsing, banner, starts uvicorn
  server.py     # FastAPI app — REST + WebSocket endpoints
  plugin.py     # pytest plugin — fires webhooks back to the server during runs
  build.py      # pytest-web-build CLI — builds the package
  static/
    index.html  # Single-page UI
    app.js      # All frontend logic (vanilla JS, no build step)
    styles.css  # Styles
```

The architecture in one sentence: the CLI starts a FastAPI server, a subprocess runs pytest with the plugin loaded, the plugin sends HTTP events to the server, and the server fans them out over WebSocket to the browser.
