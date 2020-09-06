*** Settings ***
Library        GenerateUserInfo.py

*** Keywords ***
Click Register Link
    Log To Console      .. Clicking register Link
    Click Element   ${REGISTER}

Enter username
    Log To Console      .. Entering Username
    Element Should Be Visible   ${USERNAME_INPUT}   10s
    ${username} =    create username   user
    Set Global Variable      ${username}     ${USERNAME}
    Input Text  ${USERNAME_INPUT}   ${USERNAME}

Enter Password
    Log To Console      .. Entering Password
    Element Should Be Visible   ${PASSWORD_INPUT}    10s
    ${password} =    create password
    log To Console      ${password}
    Set Global Variable      ${password}     ${PASSWORD}
    Input Text  ${PASSWORD_INPUT}   ${PASSWORD}

Enter FirstName
    Log To Console      .. Entering FirstName
    Element Should Be Visible   ${FIRSTNAME_INPUT}   10s
    Input Text  ${FIRSTNAME_INPUT}   ${FIRSTNAME}

Enter FamilyName
    Log To Console      .. Entering FamilyName
    Element Should Be Visible   ${LASTNAME_INPUT}   10s
    Input Text  ${LASTNAME_INPUT}   ${LASTNAME}

Enter PhoneNumber
    Log To Console      .. Entering PhoneNumber
    Element Should Be Visible   ${PHONENUMBER_INPUT}   10s
    ${phonenumber} =    create phonenumber
    Set Global Variable      ${phonenumber}      ${PHONENUMBER}
    Input Text  ${PHONENUMBER_INPUT}   ${PHONENUMBER}

Click Register
    log To Console      .. Clicking Register Button
    Element Should Be Visible   ${REGISTER_BUTTON}      10s
    Click Element   ${REGISTER_BUTTON}

Click Login Link
    Log To Console      .. Clicking Log In link
    Click Element   ${LOGIN}

Enter Login Username
    Log To Console      .. Entering UserName
    Element Should Be Visible   ${USERNAME_INPUT}   10s
    Input Text  ${USERNAME_INPUT}   ${username}

Enter login Password
    Log To Console      .. Entering Password
    Element Should Be Visible   ${PASSWORD_INPUT}    10s
    Input Text  ${PASSWORD_INPUT}   ${password}

Click Login
    log To Console      .. Clicking Login Button
    Element Should Be Visible   ${LOGIN_BUTTON}      10s
    Click Element   ${LOGIN_BUTTON}


