---
sidebar_position: 2
title: Installation
---

# Installation

## Requirements

- Python **3.9 or newer**
- pytest **7.0+**
- A project that already uses pytest

pytest-web installs `pytest-xdist` automatically as a dependency — you don't need to install it separately.

---

## Install from PyPI

```bash
pip install pytest-web
```

:::important
pytest-web must be installed in the **same Python environment** as your project's pytest. If your project uses a virtualenv, activate it first.
:::

---

## Installing into a virtualenv

```bash
# Activate your project's virtualenv first
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows

# Then install
pip install pytest-web
```

---

## Installing into a conda environment

```bash
conda activate my-env
pip install pytest-web
```

---

## Verify the install

```bash
pytest-web --version
```

You should see the installed version number. If you get `command not found`, check that your virtualenv is activated and its `bin/` (or `Scripts/` on Windows) is on your `PATH`.

---

## Upgrading

```bash
pip install --upgrade pytest-web
```

---

## Uninstalling

```bash
pip uninstall pytest-web
```

This removes pytest-web but leaves pytest and pytest-xdist untouched.
