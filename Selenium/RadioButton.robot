*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify radio buttons
    Open Browser    ${URL}    edge
    Maximize Browser Window

    # wait till page loads
    Wait Until Element Is Visible   xpath://input[@value='radio1']
    #click on radio button
    Click Element    xpath://input[@value='radio2']
    #click on check box3
    Click Element    xpath://input[@value='radio3']
    #close browser
    Close Browser

