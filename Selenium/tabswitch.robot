*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Switch Tab And Window
    Open Browser    ${url}    edge
    Maximize Browser Window

    #SWITCH TAB
    Click Element    xpath://a[@id='opentab']
    Sleep    2s

    Switch Window    NEW
    Sleep    2s
    Log To Console    Switched To New Tab
    Switch Window    MAIN

    #SWITCH WINDOW
    Click Element    xpath://button[@id='openwindow']
    Sleep    2s

    Switch Window    NEW
    Sleep    2s
    Log To Console    Switched To New Window
    Close Window

    Switch Window    MAIN
    Sleep    2s

    Close Browser
