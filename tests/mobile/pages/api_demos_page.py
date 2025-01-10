from tests.mobile.base.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class ApiDemosPage(BasePage):
    # Locators using resource-id and content-desc
    ACCESSIBILITY_BUTTON = ("ID", "android:id/text1")  # Using resource-id for list items
    ANIMATION_BUTTON = ("ID", "android:id/text1")
    APP_BUTTON = ("ID", "android:id/text1")
    
    # Text values for verification
    ACCESSIBILITY_TEXT = "Accessibility"
    ANIMATION_TEXT = "Animation"
    APP_TEXT = "App"
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def tap_accessibility(self):
        """Tap on Accessibility menu item."""
        elements = self.find_elements(AppiumBy.ID, self.ACCESSIBILITY_BUTTON[1])
        for element in elements:
            if element.text == self.ACCESSIBILITY_TEXT:
                element.click()
                break
        return self

    def tap_animation(self):
        """Tap on Animation menu item."""
        elements = self.find_elements(AppiumBy.ID, self.ANIMATION_BUTTON[1])
        for element in elements:
            if element.text == self.ANIMATION_TEXT:
                element.click()
                break
        return self

    def tap_app(self):
        """Tap on App menu item."""
        elements = self.find_elements(AppiumBy.ID, self.APP_BUTTON[1])
        for element in elements:
            if element.text == self.APP_TEXT:
                element.click()
                break
        return self

    def is_main_screen_displayed(self) -> bool:
        """Check if main screen is displayed."""
        try:
            elements = self.find_elements(AppiumBy.ID, self.ACCESSIBILITY_BUTTON[1])
            return any(element.text == self.ACCESSIBILITY_TEXT for element in elements)
        except:
            return False 