# tests/ui_tests/test_login.py

import pytest
from pages.login_page import LoginPage
from config.config import Config


class TestLogin:
    """
    Test class for Login functionality.

    This class contains all login-related test cases.
    Each method starting with "test_" is a separate test case.
    """

    @pytest.mark.smoke  # Tag: This is a smoke test (critical functionality)
    @pytest.mark.ui  # Tag: This is a UI test
    def test_login_with_valid_credentials(self, driver):
        """
        Test Case ID: TC_001
        Test Case: Verify successful login with valid credentials

        Steps:
        1. Open ParaBank login page
        2. Enter valid username
        3. Enter valid password
        4. Click Login button
        5. Verify "Accounts Overview" page is displayed

        Expected Result: User is logged in successfully

        Args:
            driver: Browser driver (automatically provided by conftest.py fixture)
        """

        # Step 1: Create a LoginPage object
        # This gives us access to all login page actions
        login_page = LoginPage(driver)

        # Step 2: Open the login page
        print("\n📖 Step 1: Opening ParaBank login page...")
        login_page.open_login_page()

        # Step 3: Perform login with valid credentials from config
        print(f"🔐 Step 2: Logging in with username: {Config.TEST_USERNAME}")
        login_page.login(Config.TEST_USERNAME, Config.TEST_PASSWORD)

        # Step 4: Verify login was successful
        print("✅ Step 3: Verifying login success...")
        assert login_page.is_login_successful(), "❌ FAIL: Login failed! Accounts Overview not found"

        print("🎉 TEST PASSED: User logged in successfully!")

    @pytest.mark.smoke
    @pytest.mark.ui
    def test_login_with_invalid_username(self, driver):
        """
        Test Case ID: TC_002
        Test Case: Verify login fails with invalid username

        Steps:
        1. Open ParaBank login page
        2. Enter invalid username
        3. Enter any password
        4. Click Login button
        5. Verify error message is displayed

        Expected Result: Error message "The username and password could not be verified"

        Args:
            driver: Browser driver (automatically provided by conftest.py)
        """

        # Create LoginPage object
        login_page = LoginPage(driver)

        # Open login page
        print("\n📖 Step 1: Opening ParaBank login page...")
        login_page.open_login_page()

        # Try to login with invalid username
        invalid_username = "invalid_user_12345"
        print(f"🔐 Step 2: Attempting login with invalid username: {invalid_username}")
        login_page.login(invalid_username, Config.TEST_PASSWORD)

        # Verify error message appears
        print("✅ Step 3: Verifying error message is displayed...")
        assert login_page.is_error_message_displayed(), "❌ FAIL: Error message not displayed!"

        # Also check the error message text
        error_text = login_page.get_error_message()
        print(f"📝 Error message shown: '{error_text}'")
        assert error_text != "", "❌ FAIL: Error message is empty!"

        print("🎉 TEST PASSED: Error message displayed correctly for invalid username!")

    @pytest.mark.smoke
    @pytest.mark.ui
    def test_login_with_invalid_password(self, driver):
        """
        Test Case ID: TC_003
        Test Case: Verify login fails with invalid password

        Steps:
        1. Open ParaBank login page
        2. Enter valid username
        3. Enter invalid password
        4. Click Login button
        5. Verify error message is displayed

        Expected Result: Error message "The username and password could not be verified"

        Args:
            driver: Browser driver (automatically provided by conftest.py)
        """

        # Create LoginPage object
        login_page = LoginPage(driver)

        # Open login page
        print("\n📖 Step 1: Opening ParaBank login page...")
        login_page.open_login_page()

        # Try to login with invalid password
        invalid_password = "wrong_password_123"
        print(f"🔐 Step 2: Attempting login with invalid password")
        login_page.login(Config.TEST_USERNAME, invalid_password)

        # Verify error message appears
        print("✅ Step 3: Verifying error message is displayed...")
        assert login_page.is_error_message_displayed(), "❌ FAIL: Error message not displayed!"

        # Also check the error message text
        error_text = login_page.get_error_message()
        print(f"📝 Error message shown: '{error_text}'")
        assert error_text != "", "❌ FAIL: Error message is empty!"

        print("🎉 TEST PASSED: Error message displayed correctly for invalid password!")