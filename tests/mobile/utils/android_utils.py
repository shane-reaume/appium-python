from appium.webdriver.webdriver import WebDriver
from typing import Dict, Any

class AndroidUtils:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_device_time(self) -> str:
        """Get device time."""
        return self.driver.device_time

    def get_current_activity(self) -> str:
        """Get current activity name."""
        return self.driver.current_activity

    def get_current_package(self) -> str:
        """Get current package name."""
        return self.driver.current_package

    def toggle_airplane_mode(self):
        """Toggle airplane mode."""
        self.driver.toggle_airplane_mode()

    def toggle_wifi(self):
        """Toggle WiFi."""
        self.driver.toggle_wifi()

    def get_device_info(self) -> Dict[str, Any]:
        """Get device information."""
        return {
            "platform_version": self.driver.capabilities.get("platformVersion"),
            "device_name": self.driver.capabilities.get("deviceName"),
            "automation_name": self.driver.capabilities.get("automationName")
        }

    def start_activity(self, app_package: str, app_activity: str):
        """Start a specific activity."""
        self.driver.start_activity(app_package, app_activity)

    def is_app_installed(self, package_name: str) -> bool:
        """Check if app is installed."""
        return self.driver.is_app_installed(package_name)

    def install_app(self, app_path: str):
        """Install app from path."""
        self.driver.install_app(app_path)

    def remove_app(self, app_package: str):
        """Remove app by package name."""
        self.driver.remove_app(app_package)

    def take_screenshot(self, filename: str):
        """Take screenshot and save to file."""
        self.driver.get_screenshot_as_file(filename) 