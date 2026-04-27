# General QA Practice — Pytest & Playwright

Practice repository for learning pytest and Playwright in the context of web UI and API testing.
Test target: [The Internet](https://the-internet.herokuapp.com) (fundamentals) → [Automation Exercise](https://automationexercise.com) (UI + API combined).

---

## Setup

### 1. Create and activate virtual environment

```bash
python -m venv .venv
python -m pip install --upgrade pip
```

Activate:
- **Windows (bash/Git Bash):** `source .venv/Scripts/activate`
- **Windows (CMD):** `.venv\Scripts\activate.bat`
- **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`

You should see `(.venv)` in your prompt.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers

```bash
playwright install chromium
```

Install all browsers if needed:
```bash
playwright install
```

---

## Running tests

| Command | What it does |
|---|---|
| `pytest` | Run all tests |
| `pytest tests/e2e/` | Run e2e (Playwright) tests only |
| `pytest tests/unit/` | Run unit tests only |
| `pytest tests/e2e/test_login.py` | Run a single test file |
| `pytest tests/e2e/test_login.py::test_valid_login` | Run a single test by name |
| `pytest -k "login"` | Run all tests whose name contains "login" |
| `pytest --headed` | Run browser in visible (non-headless) mode |
| `pytest --slowmo=500` | Slow down browser actions by 500ms (useful for debugging) |

Test report is generated at `playwright-report/report.html` after each run.

---

## Project structure

```
tests/
  conftest.py       # shared fixtures (browser context config)
  e2e/              # Playwright browser tests
  unit/             # Pure pytest tests (logic, mocking, parametrize)
pages/
  base_page.py      # BasePage class — inherited by all page objects
  __init__.py
```

## Completed exercises

| # | Topic | Test file |
|---|---|---|
| 1 | Login (valid / invalid) | `tests/e2e/test_login.py` |
| 2 | Logout | `tests/e2e/test_logout.py` |
| 3 | Checkboxes | `tests/e2e/test_checkboxes.py` |
| 4 | Dropdown | `tests/e2e/test_dropdown.py` |
| 5 | Tables | `tests/e2e/test_tables.py` |
| 6 | JavaScript alerts | `tests/e2e/test_alerts.py` |
| 7 | Drag and drop | `tests/e2e/test_drag_drop.py` |
| 8 | iFrame | `tests/e2e/test_iframe.py` |
| 9 | Hovers | `tests/e2e/test_hovers.py` |
| 10 | File upload | `tests/e2e/test_upload_file.py` |
| 11 | File download | `tests/e2e/test_download.py` |
| 12 | Basic auth | `tests/e2e/test_basic_auth.py` |

---

## Running modules

```
  pytest tests/unit/ -m smoke -v      # smoke only
  pytest tests/unit/ -m "not smoke" -v  # all others
```