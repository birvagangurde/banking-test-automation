# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import Config


class BasePage:
    """
    BasePage is the parent class for all page objects.
    It contains common methods that every page will need.

    Think of it like a "universal remote control" that works with any TV.
    """

    def __init__(self, driver):
        """
        Constructor - runs when you create a BasePage object

        Args:
            driver: The Selenium WebDriver (browser controller)
        """
        self.driver = driver  # Save the driver so we can use it everywhere
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)  # Helper for waiting

    def open_url(self, url):
        """
        Open a website URL

        Args:
            url: Website address (e.g., "https://google.com")
        """
        self.driver.get(url)

    def find_element(self, locator):
        """
        Find an element on the page (like finding a button)
        Waits until element appears, then returns it

        Args:
            locator: Tuple with (How to find, What to find)
                     Example: (By.ID, "username") means find element with id="username"

        Returns:
            The web element found
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """
        Click on an element (like clicking a button)

        Args:
            locator: Tuple describing which element to click
        """
        element = self.find_element(locator)  # First find it
        element.click()  # Then click it

    def type_text(self, locator, text):
        """
        Type text into an input field (like filling a form)

        Args:
            locator: Tuple describing which input field
            text: What text to type
        """
        element = self.find_element(locator)  # Find the input box
        element.clear()  # Clear any existing text
        element.send_keys(text)  # Type new text

    def get_text(self, locator):
        """
        Get the visible text from an element

        Args:
            locator: Tuple describing which element

        Returns:
            String containing the element's text
        """
        element = self.find_element(locator)
        return element.text

    def is_element_visible(self, locator, timeout=5):
        """
        Check if an element is visible on the page
        Useful for verifying if something appeared after an action

        Args:
            locator: Tuple describing which element to check
            timeout: How many seconds to wait before giving up (default: 5)

        Returns:
            True if element is visible, False if not found
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True  # Element found and visible!
        except TimeoutException:
            return False  # Element not found within timeout

    def get_page_title(self):
        """
        Get the title of the current page

        Returns:
            String containing page title
        """
        return self.driver.title