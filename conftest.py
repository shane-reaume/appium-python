import pytest
import os
import asyncio
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def appium_driver():
    """Create Appium WebDriver instance."""
    logger.info("Setting up Appium driver")
    
    # Get environment variables
    app_path = os.getenv('APP_PATH', './ApiDemos-debug.apk')
    device_name = os.getenv('DEVICE_NAME', 'Pixel_7_API_35')
    platform_version = os.getenv('PLATFORM_VERSION', '14.0')
    app_package = os.getenv('APP_PACKAGE', 'io.appium.android.apis')
    app_activity = os.getenv('APP_ACTIVITY', '.ApiDemos')
    
    # Log environment configuration
    logger.info(f"App path: {app_path}")
    logger.info(f"Device name: {device_name}")
    logger.info(f"Platform version: {platform_version}")
    logger.info(f"App package: {app_package}")
    logger.info(f"App activity: {app_activity}")
    
    # Set up capabilities using UiAutomator2Options
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.automation_name = 'UiAutomator2'
    options.device_name = device_name
    options.platform_version = platform_version
    options.app = os.path.abspath(app_path)
    options.app_package = app_package
    options.app_activity = app_activity
    options.no_reset = False
    options.auto_grant_permissions = True
    options.new_command_timeout = 300
    options.system_port = 8201
    
    # Log capabilities
    logger.info("Appium capabilities:")
    caps = options.to_capabilities()
    for key, value in caps.items():
        logger.info(f"  {key}: {value}")
    
    try:
        # Create driver with options
        logger.info("Creating Appium driver")
        driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        logger.info("Appium driver created successfully")
        
        # Set implicit wait
        driver.implicitly_wait(10)
        
        yield driver
        
        # Cleanup
        logger.info("Cleaning up Appium driver")
        try:
            if app_package:
                driver.terminate_app(app_package)
            driver.quit()
            logger.info("Appium driver cleanup completed")
        except Exception as e:
            logger.error(f"Error during driver cleanup: {str(e)}")
            
    except Exception as e:
        logger.error(f"Failed to create Appium driver: {str(e)}")
        raise

@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close() 