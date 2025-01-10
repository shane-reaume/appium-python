#!/bin/bash

# Create apps directory if it doesn't exist
mkdir -p apps

# Download Android API Demos app
echo "Downloading Android API Demos app..."
curl -L -o apps/ApiDemos-debug.apk https://raw.githubusercontent.com/appium/appium/master/packages/appium/sample-code/apps/ApiDemos-debug.apk

# Verify download
if [ -f "apps/ApiDemos-debug.apk" ]; then
    echo "✅ Successfully downloaded ApiDemos-debug.apk"
else
    echo "❌ Failed to download ApiDemos-debug.apk"
    exit 1
fi 