#check the title of the web page

import pytest

from labsessions.pages.Login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self,driver):
        lp = LoginPage(driver)
        lp.login_button("Admin", "admin123")
        assert "Dashboard" in driver.title

