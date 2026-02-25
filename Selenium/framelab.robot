*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/frames.php

*** Test Cases ***
Handle Iframes
    Open Browser    ${url}    edge
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

    # -------- IFRAME 1 ----------
    Select Frame    xpath:(//iframe)[1]
    Sleep    3s
    ${text1}=    Get Text    xpath://body
    Log To Console    Iframe1 Text: ${text1}
    Sleep    3s
    Unselect Frame

    # -------- IFRAME 2 ----------
    Select Frame    xpath:(//iframe)[2]
    Sleep    3s
    ${text2}    Get Text    xpath://body
    Log To Console    Iframe2 Text: ${text2}
    Sleep    3s
    Unselect Frame

    Close Browser