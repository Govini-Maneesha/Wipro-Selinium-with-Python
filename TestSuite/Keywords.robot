Library    SeleniumLibrary

*** Test Cases ***
# Name of the testcase
Verify login with valid credentials
           Login

Verify Add to cart functionality
           Login
    Log    User select the product
    Log    User add the product to cart
    Log    Item added to cart

*** Keywords ***
Login
    Log    Enter username
    Log    Enter password
    Log    Click on login button
    Log    User is on the home page
