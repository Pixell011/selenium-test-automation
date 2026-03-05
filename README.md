# selenium-test-automation

QA automation framework with Selenium + Pytest using Page Object Model.

## Project structure

- `pages/`: page objects
- `tests/`: test cases
- `utils/`: shared utilities
- `conftest.py`: shared pytest fixtures
- `scripts/setup_windows.ps1`: one-command Windows setup

## Quick setup (Windows)

1. Open PowerShell in the project root.
2. Create virtual environment:
   `py -m venv .venv`
3. Activate virtual environment:
   `.\.venv\Scripts\Activate.ps1`
4. Upgrade pip:
   `python -m pip install --upgrade pip`
5. Install dependencies:
   `pip install -r requirements.txt`
6. Run tests:
   `python -m pytest -q`

## One-command setup (Windows)

Run:

`powershell -ExecutionPolicy Bypass -File .\scripts\setup_windows.ps1`

This script recreates `.venv`, installs dependencies, and runs `python -m pytest -q`.

## VSCode interpreter

Use:

`Python: Select Interpreter` -> `.venv\Scripts\python.exe`

## Notes

- ChromeDriver is managed automatically by Selenium Manager.
- No `webdriver-manager` dependency is required.
- In OneDrive folders, physical deletion of `.venv` or `.pytest_cache` may fail due to file locks/permissions. They are ignored by git and should not be committed.
