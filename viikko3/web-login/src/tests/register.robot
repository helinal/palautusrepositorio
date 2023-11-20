*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  mikko
    Set Password  mikko123
    Set Password Confirmation  mikko123
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  an
    Set Password  anna123
    Set Password Confirmation  anna123
    Submit Registration
    Register Should Fail With Message  Username must be at least 3 characters and only contain the letters a-z

Register With Valid Username And Too Short Password
    Set Username  banna
    Set Password  12
    Set Password Confirmation  12
    Submit Registration
    Register Should Fail With Message  Password must be at least 8 characters and contain at least 1 number

Register With Nonmatching Password And Password Confirmation
    Set Username  aaaa
    Set Password  aaaa123
    Set Password Confirmation  aaaa333
    Submit Registration
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  jaakko
    Set Password  jaakko123
    Set Password Confirmation  jaakko123
    Submit Registration
    Go To Login Page
    Login User  jaakko  jaakko123
    Login Should Succeed

Login After Failed Registration
    Set Username  muumi
    Set Password  muumi
    Set Password Confirmation  muumi
    Submit Registration
    Go To Login Page
    Login User  muumi  muumi
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Login User
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Submit Credentials