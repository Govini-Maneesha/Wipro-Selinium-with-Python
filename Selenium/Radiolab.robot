*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/check-box.php

*** Test Cases ***
Verify the Radio and Check Buttons
           open Browser       ${url}        edge

           Maximize Browser Window

           Wait Until Element Is Visible       //body/main/div[@class='container']/div[@class='row d-flex justify-content-center logindiv bg-white rounded']/div[@class='col-md-8 col-lg-8 col-xl-8']/div[@class='tree_main']/ul[@id='bs_main']/li[@id='bs_1']/span[1]

           Sleep    3s

           Click Element    //body/main/div[@class='container']/div[@class='row d-flex justify-content-center logindiv bg-white rounded']/div[@class='col-md-8 col-lg-8 col-xl-8']/div[@class='tree_main']/ul[@id='bs_main']/li[@id='bs_1']/span[1]

           Sleep    3s

           Click Element    //input[@id='c_bs_1']

           Sleep    3s

           Click Element    //body/main/div[@class='container']/div[@class='row d-flex justify-content-center logindiv bg-white rounded']/div[@class='col-md-8 col-lg-8 col-xl-8']/div[@class='tree_main']/ul[@id='bs_main']/li[@id='bs_2']/span[1]

           Sleep    3s

           Click Element    //input[@id='c_bs_2']

           Sleep    3s

           Close Browser