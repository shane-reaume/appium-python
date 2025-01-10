import pytest
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def appium_driver(request):
    """Create and configure the Appium driver."""
    logger.info("Setting up Appium driver")
    
    # App configuration
    app_path = "./ApiDemos-debug.apk"
    device_name = "Pixel_7_API_35"
    platform_version = "15.0"
    app_package = "io.appium.android.apis"
    app_activity = ".ApiDemos"
    
    # Log the configuration
    logger.info(f"App path: {app_path}")
    logger.info(f"Device name: {device_name}")
    logger.info(f"Platform version: {platform_version}")
    logger.info(f"App package: {app_package}")
    logger.info(f"App activity: {app_activity}")
    
    # Set up UiAutomator2 options with increased timeouts
    options = UiAutomator2Options()
    options.automation_name = "UiAutomator2"
    options.platform_name = "Android"
    options.device_name = device_name
    options.platform_version = platform_version
    options.app = app_path
    options.app_package = app_package
    options.app_activity = app_activity
    options.no_reset = False
    options.auto_grant_permissions = True
    options.new_command_timeout = 300
    options.system_port = 8201
    
    # Additional settings for stability
    options.set_capability('uiautomator2ServerLaunchTimeout', 60000)  # 60 seconds
    options.set_capability('uiautomator2ServerInstallTimeout', 60000)  # 60 seconds
    options.set_capability('androidDeviceReadyTimeout', 60)  # 60 seconds
    options.set_capability('adbExecTimeout', 60000)  # 60 seconds
    options.set_capability('appWaitActivity', '*')  # Wait for any activity
    options.set_capability('autoGrantPermissions', True)
    options.set_capability('skipServerInstallation', False)
    options.set_capability('skipDeviceInitialization', False)
    
    # Log the capabilities
    logger.info("Appium capabilities:")
    for key, value in options.capabilities.items():
        logger.info(f"  {key}: {value}")
    
    # Create the driver
    logger.info("Creating Appium driver")
    try:
        driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        logger.info("Appium driver created successfully")
        
        def fin():
            logger.info("Cleaning up Appium driver")
            if driver:
                driver.quit()
            logger.info("Appium driver cleanup completed")
        
        request.addfinalizer(fin)
        return driver
    except Exception as e:
        logger.error(f"Failed to create Appium driver: {str(e)}")
        raise 