import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_dropdown():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://trytestingthis.netlify.app")
    time.sleep(2)

    # single select
    single = driver.find_element(By.ID, "option")
    driver.execute_script("arguments[0].scrollIntoView();", single)
    Select(single).select_by_visible_text("Option 2")
    time.sleep(2)

    # multi select
    multi_element = driver.find_element(By.ID, "owc")
    driver.execute_script("arguments[0].scrollIntoView();", multi_element)

    multi = Select(multi_element)
    multi.select_by_visible_text("Option 1")
    multi.select_by_visible_text("Option 2")
    time.sleep(2)

    # deselect all (correct variable)
    multi.deselect_all()
    time.sleep(2)

    driver.quit()