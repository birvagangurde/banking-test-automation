import pytest
from pages.login_page import LoginPage
from config.config import Config


class TestLogin:

    @pytest.mark.smoke
    def test_login_with_valid_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login(Config.TEST_USERNAME, Config.TEST_PASSWORD)
        assert login_page.is_login_successful()