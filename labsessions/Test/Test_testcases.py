from labsessions.pages.Home_page import HomePage

def test_testcases_page(driver):

    home = HomePage(driver)
    home.open_testcases()