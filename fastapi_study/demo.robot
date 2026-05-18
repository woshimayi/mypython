*** Settings ***
Documentation     Demo test suite for Robot Framework API

*** Test Cases ***
Simple Test
    Log    Hello from Robot Framework
    Should Be True    ${TRUE}
    Sleep    1s

Another Test
    Log    This is another test case
    ${result}=    Evaluate    1 + 1
    Should Be Equal    ${result}    ${2}
