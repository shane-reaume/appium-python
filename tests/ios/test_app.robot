*** Settings ***
Resource          ../resources/common.robot
Suite Setup       Open Application With Capabilities
Suite Teardown    Close Test Application
Test Teardown     Take Screenshot On Failure

*** Variables ***
# UI Elements in the Test App
${APP_WINDOW}    xpath=//XCUIElementTypeApplication[@name="TestApp"]
${TEXT_FIELD}    xpath=//XCUIElementTypeTextField
${BUTTON}        xpath=//XCUIElementTypeButton

*** Keywords ***
Open Application With Capabilities
    ${capabilities}=    Create Dictionary
    ...    platformName=${PLATFORM_NAME}
    ...    platformVersion=${PLATFORM_VERSION}
    ...    deviceName=${DEVICE_NAME}
    ...    automationName=${AUTOMATION_NAME}
    ...    app=${APP}
    Open Test Application    http://${APPIUM_HOST}:${APPIUM_PORT}    ${capabilities}

Log Page Source
    ${source}=    Get Source
    Log    ${source}    HTML

*** Test Cases ***
Should Show Page Source
    Log Page Source

Should Launch Application Successfully
    Element Should Be Visible And Enabled    ${APP_WINDOW}
    Page Should Contain Element    ${TEXT_FIELD}

Should Interact With App
    Wait Until Element Is Visible And Click    ${TEXT_FIELD}
    Input Text Into Element    ${TEXT_FIELD}    123
    Element Should Be Visible    ${BUTTON}
    Wait Until Element Is Visible And Click    ${BUTTON} 