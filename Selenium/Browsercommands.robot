*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://the-internet.herokuapp.com/upload

*** Test Cases ***
Verify waits
    Open Browser    ${url}    edge
    Maximize Browser Window
    Set Selenium Implicit Wait    3s
    Go Back
    Sleep    3s
    Reload Page
    Sleep    3s
    Close Browser