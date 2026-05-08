---
sidebar_position: 3
title: Features
---

# Features

## Fetch & select tests

Click **Fetch Tests** (or press `Enter` in the args bar) to collect all tests via `pytest --collect-only`. Tests are grouped by file.

From there you can:

- ✅ Check / uncheck individual tests or entire file groups
- ✅ Use **Select All** to toggle only what's currently visible (filter-aware)
- ✅ Type in the **filter box** to search by test name
- ✅ Click any counter — **passed / failed / skipped** — to filter to that status; click again to clear

:::tip
The args bar accepts any pytest collection flags. For example, type `-m smoke` to fetch only tests marked `smoke`, or `tests/api/` to collect from a specific folder.
:::

---

## Parameterized tests

Every `@pytest.mark.parametrize` variant is auto-expanded as a **separate, individually selectable row**:

```
test_addition[1-2-3]
test_addition[10-20-30]
test_addition[100-200-300]
```

No setup needed — pytest-web uses pytest's own collection, so every variant shows up exactly as pytest sees it. You can run a single combination, a subset, or all of them.

---

## Parallel runs with xdist

Set the **Workers** field to run tests in parallel using `pytest-xdist`:

| Workers | Behaviour |
|---------|-----------|
| `1` | Standard single-process pytest |
| `2+` | Runs with `-n <workers>`, distributed across processes |

pytest-xdist is installed automatically as a dependency. pytest-web handles the duplicate-event deduplication that xdist's master-worker report forwarding would otherwise cause.

---

## Run controls

- **▶ Run Selected** — runs only the checked tests that are currently visible under the active filter
- **■ Cancel** — terminates the pytest process and all xdist workers cleanly (no zombie processes)

:::note
"Run Selected" respects your current filter. If you've filtered to "failed" and unchecked a few, only the remaining visible checked tests run — hidden tests are never silently included.
:::

---

## Param builder

The dropdown lets you add common pytest flags to the args bar without typing:

- `-k` — keyword expression
- `-m` — marker expression
- `--tb` — traceback style (`short`, `long`, `no`, `line`)
- `-x` — stop on first failure
- `--maxfail` — stop after N failures
- `-s` — don't capture stdout
- `-v` — verbose output

**Project-specific options** from your `conftest.py` or installed plugins (e.g. `--browser`, `--headed` from playwright) are **auto-detected** and added to the dropdown — no configuration needed.

---

## Env var injection

Inject environment variables into the test run without touching your shell or `.env` files:

1. Click **+ Add Env Var**
2. Type `NAME=value` in the Name field — it auto-splits on blur
3. Variables are saved to `localStorage` and restored on page reload

This is useful for switching between environments (`ENV=staging`), toggling feature flags, or injecting credentials for a specific run.

---

## Live status

While tests run, each row shows a **pulsing dot** that turns:

- 🟢 **Green** — passed
- 🔴 **Red** — failed
- 🟡 **Yellow** — skipped

Counters update in real time and **accumulate across runs** — so if you run a subset, results from tests not in this run are preserved. Only a fresh **Fetch Tests** resets everything.

Failed tests show an **expand button (▾)** — click it to see the full traceback inline without leaving the page.

---

## Output log

Pytest's stdout and stderr stream into a **collapsible panel** at the bottom of the page.

- Opens automatically when stderr has content (e.g. test failures, import errors)
- Shows all xdist worker output merged into a single stream
- Line count shown in the toggle header

---

## Command preview

The `$ pytest ...` command at the bottom updates live as you change selections, args, or workers.

- Click **⎘** to copy it to your clipboard
- Useful for reproducing a run exactly in your terminal

:::note
`-k` and `-m` filters are **stripped** from the run command when you're running by explicit node IDs — they'd otherwise silently exclude tests whose names don't match the expression. The preview reflects this.
:::

---

## Themes

Use the theme selector (top-right) to switch between **Light**, **Dark**, **Purple**, **Pink**, and **Forest** themes. Your preference is saved to `localStorage`.
