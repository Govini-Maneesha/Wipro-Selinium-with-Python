*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/download

*** Test Cases ***
Verify File Download Link
    Open Browser    ${url}    edge
    Maximize Browser Window

    Wait Until Element Is Visible    xpath=//a[normalize-space()='sample-zip-file.zip']

    Click Element    xpath=//a[normalize-space()='sample-zip-file.zip']
    #check if the file is present in the folder
    ${files}=    List Files In Dictionary    C:\Users\HP\Downloads
    List Should Contain Value    ${files}    sample-zip-file.zip

    Sleep    5s
    Close Browser