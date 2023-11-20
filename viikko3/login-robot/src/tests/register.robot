*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Input New Command
    Input Credentials  kalle  kalle321
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  aa  kalle123
    Output Should Contain  Username must be over 3 characters and contain only the letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  hanna  123
    Output Should Contain  Password must be at least 8 characters and contain at least 1 character

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  hanna  aaaaaaaa
    Output Should Contain  Password must be at least 8 characters and contain at least 1 character