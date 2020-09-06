*** Settings ***
Resource    UserAction.robot

*** Keywords ***
Open Browser And Go To URL
   Log To Console       .. Opening Browser
   Open Browser     ${URL}      ${BROWSER}

Verify App Name And Page Name
    Log To Console      .. /nVerifying App And Page Name
    Element Should Be Visible   ${DEMO}     10s
    Element Should be Visible   ${PAGE}     10s

Verify Register Link Is Present
    Log To Console      .. /nVerifying Registeration Link
    Element Should Be Visible   ${REGISTER}     10s

Verify Login Link Is Present
    Log To Console      .. /nVerifying login Link
    Element Should Be Visible   ${LOGIN}     10s

Register Page Should Open
    Log To Console      .. Verifying Register Page is Open
    Page Should Contain Element     ${REGISTER_HEADER}

login Page Should Open
    Log To Console      .. Verifying Login Page is Open
    page Should Contain Element     ${LOGIN_HEADER}

User Information Page Should Open
    Log To Console      .. Verifying User Information Page is Open
    page Should Contain Element     ${USER_INFO}

Do Registration
    Log To Console      .. Registering User
    Click Register Link
    Register Page Should Open
    Enter Username
    Enter Password
    Enter FirstName
    Enter FamilyName
    Enter Phonenumber
    Click Register
    log To Console      .. User Registered.

Login User
    Log To console      ..  User Logging in
    Click Login Link
    Log In Page Should Open
    Enter Login Username
    Enter Login Password
    Click Login
    User Information Page Should Open
    Page Should Contain Element     ${USER_INFO}
