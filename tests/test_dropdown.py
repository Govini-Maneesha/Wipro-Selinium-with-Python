import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_Dropdown:

    def test_dropdown(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        time.sleep(2)

        # Locate dropdown element
        dropdown = driver.find_element(By.ID, "dropdown-class-example")

        # Create Select object
        sel = Select(dropdown)

        # Select options
        sel.select_by_visible_text("Option1")
        time.sleep(2)

        sel.select_by_visible_text("Option2")
        time.sleep(2)

        sel.select_by_index(3)
        time.sleep(2)


        driver.quit()