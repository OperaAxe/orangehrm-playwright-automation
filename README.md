# OrangeHRM — Playwright Automation

[![Playwright tests](https://github.com/OperaAxe/orangehrm-playwright-automation/actions/workflows/tests.yml/badge.svg)](https://github.com/OperaAxe/orangehrm-playwright-automation/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-Python-2EAD33?logo=playwright&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-tests-0A9EDC?logo=pytest&logoColor=white)

A focused browser-automation project for the public [OrangeHRM Open Source demo](https://opensource-demo.orangehrmlive.com/), built with **Python, Playwright, and pytest**.

The suite concentrates on observable user journeys: login, dashboard navigation, and employee-directory search. The goal is to verify outcomes and resulting page state, not just whether controls can be clicked.

## Test coverage

| Area | Scenario | Assertion |
|:--|:--|:--|
| Login | Login screen loads | Login heading, username/password fields, and public demo credential hints are visible |
| Authentication | Valid demo credentials | Browser reaches the Dashboard |
| Dashboard | Main navigation renders | Admin, PIM, Leave, Time, My Info, Performance, Dashboard, Directory, and Maintenance are visible |
| Directory | Type "manda" and pick the first matching employee from autocomplete | The search returns exactly one record for the selected employee |

The suite uses whichever matching employee the shared demo currently has, because the demo data changes over time.

## Run locally

Requires Python 3.11 or newer.

### 1. Create and activate a virtual environment

Windows PowerShell:

~~~powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
~~~

macOS / Linux:

~~~bash
python -m venv .venv
source .venv/bin/activate
~~~

### 2. Install dependencies and Chromium

~~~bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
~~~

### 3. Run the tests

~~~bash
pytest -v
~~~

Run only the smoke-marked tests:

~~~bash
pytest -m smoke -v
~~~

## Configuration

The public demo displays its own test credentials on the login page. The suite uses those demo values by default. Override the URL or credentials with environment variables when needed.

Windows PowerShell:

~~~powershell
$env:ORANGEHRM_BASE_URL="https://opensource-demo.orangehrmlive.com"
$env:ORANGEHRM_USERNAME="Admin"
$env:ORANGEHRM_PASSWORD="admin123"
pytest -v
~~~

macOS / Linux:

~~~bash
export ORANGEHRM_BASE_URL="https://opensource-demo.orangehrmlive.com"
export ORANGEHRM_USERNAME="Admin"
export ORANGEHRM_PASSWORD="admin123"
pytest -v
~~~

Only use credentials you are authorised to use. The defaults are the credentials publicly shown by the OrangeHRM demo itself; do not reuse them on any other system.

## Project structure

~~~text
.
├── .github/workflows/tests.yml
├── docs/test-plan.md
├── tests/
│   ├── conftest.py
│   ├── test_dashboard.py
│   ├── test_directory.py
│   └── test_login.py
├── .gitignore
├── pytest.ini
└── requirements.txt
~~~

## Scope and limitations

- This is a portfolio automation exercise against a shared public demo, not a client system.
- The suite performs read-only checks after authentication. It does not create, edit, or delete employees, leave requests, attendance entries, or other records.
- Demo data and availability can change. A failed run must be investigated before it is classified as an application defect.
- The suite runs locally and in GitHub Actions on every push. The badge at the top links to the latest result.

## Author

**Christian David** — Software Quality Assurance Engineer

[GitHub](https://github.com/OperaAxe) · [LinkedIn](https://www.linkedin.com/in/davidchristianj/)

> Good testing checks what the user actually experiences — then verifies the resulting state.
