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
