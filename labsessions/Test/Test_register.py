from labsessions.pages.Home_page import HomePage
from labsessions.pages.Signup_page import SignupPage

def test_register_user(driver):

    home = HomePage(driver)
    home.open_login()

    signup = SignupPage(driver)
    signup.start_signup()
    signup.complete_registration()

    assert signup.verify_account_created()