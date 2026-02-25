*** Settings ***
# Settings: add external libraries, resources, setup and teardown
Library    SeleniumLibrary


*** Test Cases ***
# Name of the testcase
Verify login with valid credentials
    Log    Enter username
    Log    Enter password
    Log    Click on login button
    Log    User is on the home page