# tests/ui_tests/conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.config import Config


@pytest.fixture(scope="function")
def driver():
    """
    This is a pytest "fixture" - a special function that runs automatically.

    Scope="function" means:
    - Before EACH test: Create a fresh new browser
    - After EACH test: Close the browser

    This ensures each test starts with a clean browser (no leftover data).

    Yields:
        driver: Selenium WebDriver instance (the browser controller)
    """

    # ========== SETUP (runs BEFORE each test) ==========
    print("\n🚀 Setting up browser...")

    # Create Chrome browser driver
    # ChromeDriverManager() automatically downloads the correct chromedriver version
    # So you don't have to manually download it!
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Configure the browser
    driver.maximize_window()  # Make browser fullscreen
    driver.implicitly_wait(Config.IMPLICIT_WAIT)  # Wait 10 seconds for elements automatically

    print("✅ Browser ready!")

    # Give the driver to the test function
    yield driver

    # ========== TEARDOWN (runs AFTER each test) ==========
    print("\n🛑 Closing browser...")
    driver.quit()  # Close browser and cleanup
    print("✅ Browser closed!")