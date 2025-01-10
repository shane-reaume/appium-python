import pytest
from tests.mobile.pages.api_demos_page import ApiDemosPage
from tests.mobile.utils.android_utils import AndroidUtils

class TestApiDemos:
    def test_app_launch(self, appium_driver):
        """Test that we can launch the app and verify basic interaction."""
        # Initialize page objects
        api_demos_page = ApiDemosPage(appium_driver)
        
        # Simple verification that we can find elements on the screen
        elements = appium_driver.find_elements(by="id", value="android:id/text1")
        assert len(elements) > 0, "No menu items found on main screen"
        
        # Basic interaction - click first menu item
        elements[0].click()
        
        # Navigate back
        appium_driver.back()
        
        # Verify we can still find elements after navigation
        elements = appium_driver.find_elements(by="id", value="android:id/text1")
        assert len(elements) > 0, "No menu items found after navigation" 