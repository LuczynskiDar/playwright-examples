# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

Study repository for practicing Playwright (e2e) and pytest (unit/mocking) skills.
Test targets: `the-internet.herokuapp.com` for fundamentals, `automationexercise.com` for UI + API combined.
**Working mode:** Claude proposes tasks and reviews code written by the user.

## Commands

```bash
# Setup (once)
python -m venv .venv
source .venv/Scripts/activate     # Windows Git Bash
pip install -r requirements.txt
playwright install chromium

# Run tests
pytest                             # all tests
pytest tests/e2e/                  # e2e only
pytest tests/unit/                 # unit only
pytest tests/e2e/test_foo.py::test_bar  # single test
pytest -k "login"                  # filter by name
pytest --headed                    # visible browser
pytest --slowmo=500                # slow down for debugging
```

Report generated at `playwright-report/report.html` after each run.

## Architecture

```
tests/
  conftest.py       # browser context fixtures (viewport, auth state)
  e2e/              # Playwright tests — one file per feature area
  unit/             # pytest tests — assertions, parametrize, mocking
pages/
  base_page.py      # BasePage with shared browser actions (navigate, get_title)
                    # all page objects inherit from this
```

**Page Object Model:** each page under test gets its own class in `pages/` that inherits `BasePage`. Tests import page classes and never call Playwright directly — selectors and flows live in page classes, assertions live in tests.

## Study progression

1. **Playwright basics** — navigation, locators, assertions, forms (`tests/e2e/`)
2. **Page Object Model** — extract page classes into `pages/`
3. **pytest fundamentals** — fixtures, parametrize, markers (`tests/unit/`)
4. **Mocking & patching** — `unittest.mock`, `pytest-mock` (`tests/unit/`)
