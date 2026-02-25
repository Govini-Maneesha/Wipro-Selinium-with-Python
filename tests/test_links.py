import os.path
import time
from itertools import count

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

DOWNLOAD_DIR="C://Users//HP//Downloads"
class Test_links:
    def test_link(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        links = driver.find_elements(By.TAG_NAME, "a")
        count = len(links)
        print(count)

        for link in links:
            print(link.text)

        time.sleep(2)
        driver.close()