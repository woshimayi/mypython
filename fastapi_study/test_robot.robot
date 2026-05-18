*** Settings ***
Documentation     pytest 对比测试 - Robot 版本

*** Test Cases ***
Simple Test
    Log    Hello from Robot Framework
    Should Be True    ${TRUE}
    ${result}=    Evaluate    1 + 1
    Should Be Equal    ${result}    ${2}

Another Test
    Log    This is another test case
    ${name}=    Set Variable    Robot Framework
    Should Be Equal    ${name}    Robot Framework
