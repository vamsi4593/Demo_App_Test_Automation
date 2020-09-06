*** Settings ***
Documentation    Suite description
Library          SeleniumLibrary
Resource         ../Resources/variables.robot
Resource         ../Resources/Utility.robot
Test Setup       Open Browser And Go To URL
Test TearDown    Close Browser

*** Test Cases ***
Verify Index Page
    [Tags]    TC1
    Verify App Name And Page Name
    Verify Register Link Is Present
    Verify Login Link Is Present

Register User
    [Tags]     TC2
    Verify Register Link Is Present
    Do Registration

Login User
    [Tags]     TC3
    verify login Link Is Present
    Login user




