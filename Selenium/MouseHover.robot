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
    Mouse Over    xpath=//div[@class='container']//div[1]//img[1]
    Sleep    2s
    Element Should Be Visible    xpath://h5[normalize-space()='name: user1']

    Close Browser

