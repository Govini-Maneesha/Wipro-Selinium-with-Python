import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_grid_execution():
    options = Options()

    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=options
    )

    driver.get("https://www.google.com")
    print("Title is:", driver.title)

    driver.quit()