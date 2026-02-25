*** Settings ***
# Settings: add external libraries, resources, setup and teardown
Resource    ./../Resources/Resource.robot
Library    SeleniumLibrary
Test Setup    Launch Browser
Test Teardown    Closing Browser


*** Test Cases ***
# Name of the testcase
Verify login with valid credentials
           Login

Verify Add to cart functionality
           Login
    Log    User selects the product
    Log    User adds the product to the cart
    Log    User verifies that the product with details is added to the cart