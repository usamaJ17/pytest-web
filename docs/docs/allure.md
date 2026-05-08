---
sidebar_position: 5
title: Allure Reports
---

# Allure Reports

pytest-web has built-in support for generating and serving [Allure](https://allurereport.org/) reports — with **automatic history tracking** so trend graphs work out of the box.

---

## Requirements

### 1. Allure CLI

Install the Allure command-line tool globally (this is a separate Java-based tool, not the Python package):

- [Allure installation guide](https://allurereport.org/docs/v3/install/)

Verify it's on your PATH:

```bash
allure --version
```

### 2. allure-pytest Python package

```bash
pip install allure-pytest
```

---

## Project setup

Add `--alluredir` to your `pytest.ini` (or `pyproject.toml`):

```ini title="pytest.ini"
[pytest]
addopts = --alluredir=test/allure-results --clean-alluredir
```

```toml title="pyproject.toml"
[tool.pytest.ini_options]
addopts = "--alluredir=test/allure-results --clean-alluredir"
```

pytest-web **auto-detects** this path from your config file. You can also enter or override it manually in the Allure bar at the bottom of the UI.

---

## Usage

1. **Run your tests** — this populates the results directory with Allure JSON files
2. **Click "Open Report"** in the Allure bar at the bottom of the page
3. The report is generated and served — your browser opens it automatically
4. The URL is shown as a clickable link in case the browser doesn't open

Click **Stop** to shut down the Allure server when you're done.

---

## History & trend graphs

Every time you click **Open Report**, pytest-web automatically:

1. Copies the history from the previous report back into your results directory
2. Regenerates the report with that history included

This means Allure's **trend graphs, history tabs, and retry counts work automatically** — no manual `history/` folder management required.

The report is written to `allure-report/` next to your results directory:

```
test/
  allure-results/    ← pytest writes JSON here
  allure-report/     ← pytest-web generates HTML here
```

---

## Notes

:::note Independent server
The Allure server is completely independent of the test runner. You can run tests while the Allure server is up, and the report will update on the next "Open Report" click.
:::

:::note Allure 3 compatibility
pytest-web uses Python's built-in `http.server` to serve the report rather than `allure open`, because `allure open` was removed in Allure 3. This gives identical behaviour on both Allure 2 and Allure 3, with a deterministic URL and reliable stop/restart.
:::
