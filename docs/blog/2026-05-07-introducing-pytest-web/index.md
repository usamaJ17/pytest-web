---
slug: introducing-pytest-web
title: "Stop editing your test files just to run a subset — use pytest-web instead"
authors: usama
tags: [pytest, testing, python, developer-tools, allure]
description: pytest-web gives you a browser UI for running pytest — pick exact tests, watch live results, re-run only failures, and open Allure reports in one click. No more editing files or memorising node IDs.
---

You've been there. You have a test file with 40 parametrized cases. You need to run 3 of them. So you open the file, comment out the ones you don't want, run pytest, then uncomment everything again. Or you try to remember the exact `-k` expression. Or you copy-paste a node ID from the terminal and hope you got it right.

There's a better way.

{/* truncate */}

## What is pytest-web?

pytest-web is a local web UI that sits on top of your existing pytest setup. You run one command, a browser tab opens, and from there you can see all your tests, pick exactly which ones to run, watch them pass or fail in real time, and re-run failures with a single click.

It doesn't replace pytest. It doesn't touch your `conftest.py` or your fixtures. It just wraps the same `pytest` command you already use and gives you a visual layer on top.

---

## Getting started takes 30 seconds

```bash
pip install pytest-web
cd your-project
pytest-web
```

That's it. A browser tab opens at `http://127.0.0.1:8000`. Your project's `pytest.ini`, fixtures, and plugins are all picked up automatically — nothing to configure.

---

## The parametrize problem, solved

Here's the situation that motivated this tool. Say you have this in your test file:

```python
@pytest.mark.parametrize("browser,env", [
    ("chrome",  "staging"),
    ("chrome",  "production"),
    ("firefox", "staging"),
    ("firefox", "production"),
    ("safari",  "staging"),
    ("safari",  "production"),
])
def test_checkout_flow(browser, env):
    ...
```

Six variants. You've just pushed a fix and you only want to run the two `production` ones to verify. 

**Before pytest-web:** comment out 4 parametrize entries, run pytest, uncomment them. Or write `-k "production"` and hope that expression doesn't accidentally catch something else.

**With pytest-web:** click **Fetch Tests**. Every variant appears as its own row:

```
✅  test_checkout_flow[chrome-staging]
✅  test_checkout_flow[chrome-production]
✅  test_checkout_flow[firefox-staging]
✅  test_checkout_flow[firefox-production]
✅  test_checkout_flow[safari-staging]
✅  test_checkout_flow[safari-production]
```

Uncheck the four staging ones. Click **▶ Run Selected**. Done. Your file is untouched.

---

## Watch results in real time

While tests run, each row shows a pulsing dot. As each test finishes it turns:

- 🟢 Green — passed
- 🔴 Red — failed  
- 🟡 Yellow — skipped

You don't wait for the whole suite to finish. You see results as they happen. If something fails early you already know while the rest are still running.

---

## Re-run only the failures

This is the feature people end up using the most.

After a run, click the **failed** counter at the top. The view filters to show only failed tests. Click **▶ Run Selected**. Only those tests run — nothing else.

No `-k` expression. No copy-pasting node IDs. No editing any file. Just two clicks.

This loop — run → filter to failed → fix → re-run failures — is where pytest-web saves the most time day to day.

---

## Run tests in parallel

Set the **Workers** field to any number and pytest-web runs your suite with `pytest-xdist` automatically. No config changes needed:

- Workers: `1` → normal sequential run
- Workers: `4` → 4 parallel processes

pytest-xdist is installed as a dependency, so it's already there. pytest-web handles all the complexity of deduplicating events from parallel workers so the UI stays correct.

---

## Inject env vars without touching your shell

Need to run tests against a different environment? Use the **Env Vars** panel:

| Name | Value |
|------|-------|
| `ENV` | `staging` |
| `API_URL` | `https://api.staging.example.com` |

Variables are saved to localStorage and restored on page reload. Type `NAME=value` in the Name field and it auto-splits — no need to fill both columns separately.

---

## Allure reports in one click

If you use Allure for test reporting, pytest-web has you covered. After your tests run:

1. Click **Open Report** in the Allure bar at the bottom
2. pytest-web generates the report and opens it in your browser automatically
3. Every time you regenerate, history is carried forward — so trend graphs and retry counts work out of the box

No commands to remember. No manual `allure generate && allure open`. Just one click.

---

## Everything you need, nothing you don't

Here's the full feature list — and notice how short it is:

| Feature | How it works |
|---------|-------------|
| Fetch tests | Click "Fetch Tests" or press Enter |
| Select/deselect | Checkboxes per test or per file |
| Filter by name | Type in the search box |
| Filter by outcome | Click passed / failed / skipped counter |
| Parallel workers | Set the number in the Workers field |
| Custom pytest args | Type in the args bar or use the param builder dropdown |
| Env var injection | Add rows in the Env Vars panel |
| Live output log | Collapsible panel at the bottom, opens on errors |
| Copy command | Click ⎘ to copy the exact pytest command |
| Allure report | Click "Open Report" in the Allure bar |
| Dark mode | Theme switcher in the top right |

---

## Try it now

```bash
pip install pytest-web
cd your-project
pytest-web
```

If you run into anything or have a feature idea, [open an issue on GitHub](https://github.com/usamaJ17/pytest-web/issues). The project is MIT licensed and contributions are very welcome.
