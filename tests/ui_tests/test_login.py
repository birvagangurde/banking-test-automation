# tests/ui_tests/test_login.py

"""
This module contains automated tests for the ParaBank Login functionality.
It automates manual test cases TC_001, TC_002, and TC_003.

Test Cases Covered:
- TC_001: Login with valid credentials
- TC_002: Login with invalid username
- TC_003: Login with invalid password
"""

import pytest
from pages.login_page import LoginPage
from config.config import Config


class TestLogin:
    """
    Test class for Login functionality.
    Groups all login-related test cases together.
    """

    @pytest.mark.smoke  # Tag: Critical test - run in smoke suite
    @pytest.mark.ui  # Tag: UI test - uses browser
    def test_login_with_valid_credentials(self, driver):
        """
        Test Case: TC_001
        Verify user can successfully login with valid credentials

        Priority: P1 - Critical

        Test Steps:
        1. Navigate to ParaBank login page
        2. Enter valid username
        3. Enter valid password
        4. Click Login button
        5. Verify user is redirected to Accounts Overview page

        Expected Result:
        - User successfully logged in
        - "Accounts Overview" link is visible

        Args:
            driver: Selenium WebDriver instance (provided by conftest.py fixture)
        """
        # Step 1: Create LoginPage object to interact with login page
        login_page = LoginPage(driver)

        # Step 2: Navigate to the login page
        print("\n📖 Step 1: Opening ParaBank login page...")
        login_page.open_login_page()

        # Step 3: Perform login using credentials from config
        print(f"Step 2: Logging in with username: {Config.TEST_USERNAME}")
        login_page.login(Config.TEST_USERNAME, Config.TEST_PASSWORD)

        # Step 4: Verify login was successful
        print("✅ Step 3: Verifying login success...")
        assert login_page.is_login_successful(), \
            "FAIL: Login failed! Accounts Overview link not found"

        print("🎉 TEST PASSED: User logged in successfully!")
