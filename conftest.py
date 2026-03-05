from pathlib import Path

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
