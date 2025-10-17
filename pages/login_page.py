# pages/login_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config


class LoginPage(BasePage):
    """
    LoginPage handles all actions on the ParaBank login page.
    It inherits from BasePage, so it can use all BasePage methods.

    This class knows:
    - Where the username field is
    - Where the password field is
    - Where the login button is
    - How to perform login
    - How to check if login succeeded/failed
    """

    # ==================== LOCATORS ====================
    # These are "addresses" of elements on the page
    # If the website changes, we only update these locators in ONE place!

    # By.NAME means "find by name attribute in HTML"
    # Example: <input name="username"> can be found with By.NAME, "username"
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")

    # By.XPATH means "find using XPath expression"
    # XPath is like a GPS coordinate for elements
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")

    # By.CSS_SELECTOR means "find using CSS selector"
    # CSS selectors are like styling rules
    ERROR_MESSAGE = (By.CSS_SELECTOR, "p.error")

    # By.LINK_TEXT means "find a link by its visible text"
    ACCOUNT_OVERVIEW_LINK = (By.LINK_TEXT, "Accounts Overview")

    def __init__(self, driver):
        """
        Constructor - runs when you create a LoginPage object

        Args:
            driver: Selenium WebDriver (browser controller)
        """
        super().__init__(driver)  # Call BasePage's constructor first

    # ==================== ACTIONS ====================

    def open_login_page(self):
        """
        Navigate to the ParaBank login page
        Uses the BASE_URL from config.py
        """
        self.open_url(Config.BASE_URL)

    def enter_username(self, username):
        """
        Type username into the username field

        Args:
            username: The username string to enter
        """
        self.type_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        """
        Type password into the password field

        Args:
            password: The password string to enter
        """
        self.type_text(self.PASSWORD_FIELD, password)

    def click_login_button(self):
        """
        Click the 'Log In' button
        """
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """
        Perform complete login action (combines all steps)
        This is a "convenience method" - does everything at once!

        Args:
            username: Username to login with
            password: Password to login with

        Usage:
            login_page.login("john", "demo")
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    # ==================== VERIFICATIONS ====================

    def is_login_successful(self):
        """
        Check if login was successful
        We know login succeeded if "Accounts Overview" link appears

        Returns:
            True if login successful, False otherwise
        """
        return self.is_element_visible(self.ACCOUNT_OVERVIEW_LINK)

    def get_error_message(self):
        """
        Get the error message text when login fails

        Returns:
            String containing error message, or empty string if no error
        """
        if self.is_element_visible(self.ERROR_MESSAGE, timeout=3):
            return self.get_text(self.ERROR_MESSAGE)
        return ""  # No error message found

    def is_error_message_displayed(self):
        """
        Check if an error message is displayed

        Returns:
            True if error message visible, False otherwise
        """
        return self.is_element_visible(self.ERROR_MESSAGE, timeout=3)