*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://practice.expandtesting.com/hovers
*** Test Cases ***
Verify radio buttons
    Open Browser    ${url}    edge
    #maximise brower
    Maximize Browser Window
    Sleep    3s

    Wait Until Element Is Visible    xpath=//div[@class='container']//div[1]//img[1]
    Sleep    3s
    Capture Page Screenshot    C:\Users\HP\Downloads
    Sleep    2s
    Capture Element Screenshot    xpath://div[@class='container']//div[1]//img[1]    C:\Users\HP\Downloads

    Close Browser

