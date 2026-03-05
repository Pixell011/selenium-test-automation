from pathlib import Path
from datetime import datetime

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    project_root = Path(__file__).resolve().parent
    chrome_profile_dir = project_root / ".chrome-profile"
    chrome_profile_dir.mkdir(parents=True, exist_ok=True)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(f"--user-data-dir={chrome_profile_dir}")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or report.passed:
        return

    driver_instance = item.funcargs.get("driver")
    if driver_instance is None:
        return

    screenshots_dir = Path(__file__).resolve().parent / "reports" / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"{item.name}_{timestamp}.png"
    screenshot_path = screenshots_dir / screenshot_name

    driver_instance.save_screenshot(str(screenshot_path))
