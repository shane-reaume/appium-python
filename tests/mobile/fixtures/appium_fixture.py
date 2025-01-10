import asyncio
import pytest
import logging
from appium.webdriver.webdriver import WebDriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from typing import AsyncGenerator

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AppiumHelper:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = logging.getLogger(__name__)
    
    async def find_and_click(self, locator: tuple, timeout: int = 10) -> None:
        """Find element and click with explicit wait."""
        try:
            self.logger.info(f"Finding and clicking element: {locator}")
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Successfully clicked element: {locator}")
        except TimeoutException as e:
            self.logger.error(f"Timeout waiting for element: {locator}")
            raise TimeoutException(f"Element not clickable: {locator}") from e
        
    async def find_and_send_keys(self, locator: tuple, text: str, timeout: int = 10) -> None:
        """Find element and send keys with explicit wait."""
        try:
            self.logger.info(f"Finding element to send keys: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()  # Clear existing text
            element.send_keys(text)
            self.logger.info(f"Successfully sent keys to element: {locator}")
        except TimeoutException as e:
            self.logger.error(f"Timeout waiting for element: {locator}")
            raise TimeoutException(f"Element not found: {locator}") from e
    
    async def wait_for_text(self, text: str, timeout: int = 10) -> None:
        """Wait for text to be present on the page."""
        try:
            self.logger.info(f"Waiting for text: {text}")
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')
                )
            )
            self.logger.info(f"Successfully found text: {text}")
        except TimeoutException as e:
            self.logger.error(f"Timeout waiting for text: {text}")
            raise TimeoutException(f"Text not found: {text}") from e
    
    async def scroll_to_text(self, text: str) -> None:
        """Scroll to element with specific text."""
        try:
            self.logger.info(f"Scrolling to text: {text}")
            selector = (
                MobileBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
                f'new UiSelector().text("{text}"))'
            )
            element = self.wait.until(EC.presence_of_element_located(selector))
            element.click()
            self.logger.info(f"Successfully scrolled to and clicked text: {text}")
        except TimeoutException as e:
            self.logger.error(f"Timeout scrolling to text: {text}")
            raise TimeoutException(f"Text not found after scrolling: {text}") from e

def create_driver() -> WebDriver:
    """Create and return an Appium driver with proper capabilities."""
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.automation_name = 'UiAutomator2'
    options.device_name = 'Pixel_7_API_35'
    options.app = './ApiDemos-debug.apk'
    options.auto_grant_permissions = True
    
    return WebDriver(
        command_executor='http://localhost:4723/wd/hub',
        options=options
    )

@pytest.fixture
async def appium_helper() -> AsyncGenerator[AppiumHelper, None]:
    """Fixture to provide AppiumHelper instance with driver setup and teardown."""
    logger.info("Setting up Appium driver")
    driver = create_driver()  # This is now synchronous
    helper = AppiumHelper(driver)
    
    try:
        yield helper
    finally:
        logger.info("Tearing down Appium driver")
        if driver:
            driver.quit() 