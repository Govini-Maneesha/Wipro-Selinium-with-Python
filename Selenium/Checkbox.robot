*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://www.tutorialspoint.com/selenium/practice/check-box.php

*** Test Cases ***
Verify radio buttons
    Open Browser    ${URL}    edge
    Maximize Browser Window

    # wait till page loads
    Wait Until Element Is Visible   xpath://input[@id='c_bs_1']
    #click on radio button
    Click Element    xpath://input[@id='c_bs_2']
    Sleep    5s
    #click on check box3

    #close browser
    Close Browser