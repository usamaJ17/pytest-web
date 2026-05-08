---
sidebar_position: 4
title: CLI Reference
---

# CLI Reference

## `pytest-web`

Start the web UI server for your project.

```bash
pytest-web [OPTIONS]
```

### Options

| Flag | Default | Description |
|------|---------|-------------|
| `--port PORT` | `8000` | Port to listen on |
| `--host HOST` | `127.0.0.1` | Bind host |
| `--cwd PATH` | current directory | Project root — the directory where `pytest.ini` / `pyproject.toml` lives |
| `--no-browser` | — | Skip auto-opening the browser tab on startup |
| `--version` | — | Print the installed version and exit |

### Examples

```bash
# Run from your project root (most common)
cd /path/to/your/project
pytest-web

# Custom port
pytest-web --port 9000

# Point at a specific project directory
pytest-web --cwd /path/to/your/project

# Don't open the browser automatically (useful in CI previews or remote machines)
pytest-web --no-browser

# Bind to all interfaces (e.g. to access from another machine on the network)
pytest-web --host 0.0.0.0 --port 8000
```

:::warning
Binding to `0.0.0.0` exposes the server on your local network. pytest-web is a local development tool — don't expose it to the public internet.
:::

---

## `pytest-web-build`

Build the distributable package (for maintainers / contributors only).

```bash
pytest-web-build
```

This runs the full build pipeline: bumps the version from git tags, builds the wheel and sdist, and outputs them to `dist/`. You won't need this unless you're cutting a release.
