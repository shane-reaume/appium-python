import { test as base } from '@playwright/test';
import { Remote } from 'appium/build/lib/driver';
import { AppiumDriver } from 'appium/build/lib/appium';
import * as dotenv from 'dotenv';

dotenv.config();

// Extend the base test type with our Appium fixture
export const test = base.extend<{
  appiumDriver: Remote;
}>({
  appiumDriver: async ({}, use) => {
    // Get environment variables
    const appPath = process.env.APP_PATH || './ApiDemos-debug.apk';
    const deviceName = process.env.DEVICE_NAME || 'Pixel_7_API_35';
    const platformVersion = process.env.PLATFORM_VERSION || '15.0';
    const appPackage = process.env.APP_PACKAGE || 'io.appium.android.apis';
    const appActivity = process.env.APP_ACTIVITY || '.ApiDemos';

    // Set up desired capabilities
    const capabilities = {
      platformName: 'Android',
      automationName: 'UiAutomator2',
      deviceName,
      platformVersion,
      app: appPath,
      appPackage,
      appActivity,
      noReset: false,
      fullReset: true,
      autoGrantPermissions: true,
    };

    // Create Appium driver
    const driver = await AppiumDriver.createSession({
      capabilities,
      connectionConfig: {
        hostname: 'localhost',
        port: 4723,
        protocol: 'http',
      },
    });

    // Use the driver in the test
    await use(driver);

    // Cleanup after test
    await driver.deleteSession();
  },
});

export { expect } from '@playwright/test'; 