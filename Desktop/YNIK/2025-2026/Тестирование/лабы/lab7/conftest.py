import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    """Configure ChromeDriver for UI tests."""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # Allow running in headless mode via env to simplify CI usage.
    if os.getenv("HEADLESS", "false").lower() in {"1", "true", "yes"}:
        chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options,
    )
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.fixture
def base_url():
    return "https://ya.ru"

