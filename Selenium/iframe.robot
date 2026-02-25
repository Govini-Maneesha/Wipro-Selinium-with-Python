*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://jqueryui.com/datepicker/

*** Test Cases ***
Verify waits
    Open Browser    ${url}    edge
    Maximize Browser Window
    Set Selenium Implicit Wait    3s
    Wait Until Element Is Visible    xpath://h1[normalize-space()='Datepicker']
    Select Frame    xpath://iframe[@class='demo-frame']
    Sleep    3s
    Click Element    xpath://input[@id='datepicker']
    Sleep    3s
    Click Element    xpath://a[normalize-space()='21']
    Close Browser

