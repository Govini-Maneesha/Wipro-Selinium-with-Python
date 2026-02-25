from labsessions.pages.Home_page import HomePage
from labsessions.pages.Login_page import LoginPage

def test_logout(driver):

    home = HomePage(driver)
    home.open_login()

    login = LoginPage(driver)
    login.login("testuser123@gmail.com","123456")

    home.logout()