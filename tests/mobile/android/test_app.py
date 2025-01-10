import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Test configuration
APPIUM_SERVER = 'http://localhost:4723'
CAPS = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'Pixel_7_API_35',
    'app': './ApiDemos-debug.apk',
    'autoGrantPermissions': True
}

@pytest.fixture
def driver():
    """Set up and tear down the Appium driver."""
    logger.info("Setting up Appium driver")
    driver = webdriver.Remote(APPIUM_SERVER, CAPS)
    yield driver
    logger.info("Tearing down Appium driver")
    driver.quit()

def test_app_launch(driver):
    """Test basic app launch and verification."""
    logger.info("Starting app launch test")
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "API Demos"))
    )
    assert element.is_displayed()
    logger.info("App launch test completed successfully")

def test_custom_title_interaction(driver):
    """Test interaction with the Custom Title feature."""
    logger.info("Starting custom title interaction test")
    wait = WebDriverWait(driver, 10)
    
    # Navigate to Views
    logger.info("Navigating to Views")
    views = wait.until(
        EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Views"))
    )
    views.click()
    
    # Navigate to Custom
    logger.info("Navigating to Custom")
    custom = wait.until(
        EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Custom"))
    )
    custom.click()
    
    # Click on Custom Title
    logger.info("Clicking Custom Title")
    driver.find_element(
        MobileBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Custom Title"))'
    ).click()
    
    # Interact with text fields
    logger.info("Interacting with text fields")
    left_text = wait.until(
        EC.presence_of_element_located((MobileBy.ID, "io.appium.android.apis:id/left_text"))
    )
    right_text = driver.find_element(MobileBy.ID, "io.appium.android.apis:id/right_text")
    
    left_text.clear()
    left_text.send_keys("Left Title")
    right_text.clear()
    right_text.send_keys("Right Title")
    
    # Apply changes
    logger.info("Applying text changes")
    driver.find_element(MobileBy.ACCESSIBILITY_ID, "Change Left").click()
    driver.find_element(MobileBy.ACCESSIBILITY_ID, "Change Right").click()
    
    # Verify changes
    logger.info("Verifying text changes")
    assert wait.until(
        EC.presence_of_element_located((MobileBy.XPATH, "//*[@text='Left Title']"))
    ).is_displayed()
    assert wait.until(
        EC.presence_of_element_located((MobileBy.XPATH, "//*[@text='Right Title']"))
    ).is_displayed()
    
    logger.info("Custom title interaction test completed successfully") 