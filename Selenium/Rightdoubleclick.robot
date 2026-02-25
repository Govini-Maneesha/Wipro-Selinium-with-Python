*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.amazon.in/
*** Test Cases ***
Verify radio buttons
    Open Browser    ${url}    edge
    #maximise brower
    Maximize Browser Window
    Sleep    3s

    Wait Until Element Is Visible    xpath=//a[normalize-space()='Sell']
    Open Context Menu    link=Sell
    Sleep    3s
    Double Click Element    xpath=//a[normalize-space()='Mobiles']
    Sleep    2s

    Close Browser

