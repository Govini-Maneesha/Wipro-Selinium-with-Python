*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Handle All Alerts
    Open Browser    ${URL}    edge
    Maximize Browser Window
    Wait Until Element Is Visible    xpath:(//button)[1]

    #SIMPLE ALERT
    Click Element    xpath:(//button)[1]
    Sleep    2s
    Handle Alert    action=ACCEPT    timeout=3

    #CONFIRM ALERT
    Click Element    xpath:(//button)[2]
    Sleep    5s
    Handle Alert    action=DISMISS    timeout=3

    #PROMPT ALERT
    Click Element    xpath:(//button)[3]
    Input Text Into Alert    Hello

    Sleep    5s
    Close Browser