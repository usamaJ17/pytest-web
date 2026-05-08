---
slug: /
sidebar_position: 1
title: Introduction
---

# pytest-web

[![PyPI version](https://img.shields.io/pypi/v/pytest-web.svg)](https://pypi.org/project/pytest-web/)
[![Python versions](https://img.shields.io/pypi/pyversions/pytest-web.svg)](https://pypi.org/project/pytest-web/)
[![CI](https://github.com/usamaJ17/pytest-web/actions/workflows/ci.yml/badge.svg)](https://github.com/usamaJ17/pytest-web/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**A lightweight local web UI for discovering, selecting, and running pytest suites** — with real-time pass/fail status, filtering, env-var injection, and on-demand Allure reports.

---

## Install

```bash
pip install pytest-web
```

Must be installed in the **same Python environment** as your project's pytest.

---

## Quick start

```bash
cd your-project
pytest-web
```

Opens `http://127.0.0.1:8000` in your browser automatically.

That's it. No config files, no setup — pytest-web discovers your tests using your existing `pytest.ini`, `conftest.py`, and fixtures.

---

## What you get

- **Fetch & select tests** — collect your whole suite, check/uncheck individual tests or entire files
- **Run in parallel** — built-in xdist support, just set the workers count
- **Live status** — every test row updates in real time as it runs
- **Filter by outcome** — click passed / failed / skipped to focus on what matters
- **Env var injection** — pass environment variables to the test process without touching your shell
- **Allure reports** — generate and serve Allure reports with history tracking, in one click
- **Zero interference** — your `conftest.py`, fixtures, and plugins all work exactly as normal

---

## Next steps

- [Installation](./installation) — pip, virtualenv, and project setup
- [Features](./features) — full walkthrough of every feature
- [CLI Reference](./cli-reference) — all flags and options
- [Allure Reports](./allure) — setting up Allure integration
- [How It Works](./how-it-works) — architecture overview
- [Contributing](./contributing) — run it locally and send a PR
