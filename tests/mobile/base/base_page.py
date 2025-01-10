from typing import List, Tuple
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator_type: str, locator_value: str, timeout: int = 10):
        """Find a single element with wait."""
        try:
            by = self._get_locator_type(locator_type)
            return self.wait.until(
                EC.presence_of_element_located((by, locator_value))
            )
        except TimeoutException:
            raise TimeoutException(f"Element not found with {locator_type}: {locator_value}")

    def find_elements(self, locator_type: str, locator_value: str, timeout: int = 10) -> List:
        """Find multiple elements with wait."""
        try:
            by = self._get_locator_type(locator_type)
            return self.wait.until(
                EC.presence_of_all_elements_located((by, locator_value))
            )
        except TimeoutException:
            return []

    def click_element(self, locator_type: str, locator_value: str):
        """Click element with wait."""
        by = self._get_locator_type(locator_type)
        element = self.wait.until(
            EC.element_to_be_clickable((by, locator_value))
        )
        element.click()

    def send_keys(self, locator_type: str, locator_value: str, text: str):
        """Send keys to element with wait."""
        element = self.find_element(locator_type, locator_value)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator_type: str, locator_value: str, timeout: int = 5) -> bool:
        """Check if element is visible."""
        try:
            by = self._get_locator_type(locator_type)
            self.wait.until(
                EC.visibility_of_element_located((by, locator_value))
            )
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, locator_type: str, locator_value: str):
        """Scroll to element using Android UI Automator."""
        self.driver.execute_script(
            'mobile: scrollGesture',
            {
                'left': 100, 'top': 100, 'width': 200, 'height': 200,
                'direction': 'down',
                'percent': 0.75
            }
        )

    def wait_for_element_to_disappear(self, locator_type: str, locator_value: str, timeout: int = 10):
        """Wait for element to disappear."""
        by = self._get_locator_type(locator_type)
        self.wait.until(
            EC.invisibility_of_element_located((by, locator_value))
        )

    def get_text(self, locator_type: str, locator_value: str) -> str:
        """Get element text with wait."""
        element = self.find_element(locator_type, locator_value)
        return element.text

    def _get_locator_type(self, locator_type: str):
        """Convert string locator type to AppiumBy attribute."""
        locator_map = {
            'ACCESSIBILITY_ID': AppiumBy.ACCESSIBILITY_ID,
            'CLASS_NAME': AppiumBy.CLASS_NAME,
            'ID': AppiumBy.ID,
            'NAME': AppiumBy.NAME,
            'XPATH': AppiumBy.XPATH,
            'CSS_SELECTOR': AppiumBy.CSS_SELECTOR,
            'TAG_NAME': AppiumBy.TAG_NAME,
            '-android uiautomator': AppiumBy.ANDROID_UIAUTOMATOR,
            'ANDROID_VIEWTAG': AppiumBy.ANDROID_VIEWTAG,
            'IOS_PREDICATE': AppiumBy.IOS_PREDICATE,
            'IOS_CLASS_CHAIN': AppiumBy.IOS_CLASS_CHAIN
        }
        return locator_map.get(locator_type, AppiumBy.ID) 