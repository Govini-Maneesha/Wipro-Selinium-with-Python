from selenium.webdriver.common.by import By
class LoginPage:
    username_input = (By.NAME,"username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH,"//input[@placeholder='Password']")
    dashboard_text = (By.XPATH, "//div[@class='orangehrm-login-branding']")

    def __init__(self,driver):
        self.driver = driver
    def enter_username(self,username):
        self.driver.find_element(self.username_input).send_keys(username)
    def enter_password(self, password):
        self.driver.find_element(self.password_input).send_keys(password)