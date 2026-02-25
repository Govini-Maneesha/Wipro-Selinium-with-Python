from labsessions.pages.Home_page import HomePage
from labsessions.pages.Contact_page import ContactPage

def test_contact_form(driver):

    home = HomePage(driver)
    home.open_contact()

    contact = ContactPage(driver)
    contact.fill_form()

    assert contact.success_msg()