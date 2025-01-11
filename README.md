# Mobile Test Automation Framework

A Python-based mobile test automation framework using Appium for Android and iOS (WIP) testing.

## Features

- Android app testing using Appium
- Page Object Model (POM) design pattern
- Pytest test runner with fixtures
- Configurable test environments
- Detailed logging and reporting
- iOS support (Work in Progress)

## Prerequisites

- Python 3.11 or higher
- Node.js and npm
- Appium 2.0 or higher
- Android SDK and platform tools
- Xcode (for iOS testing - coming soon)
- Java JDK 11 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/shane-reaume/appium-python.git
cd appium-python
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Appium and required drivers:
```bash
npm install -g appium
appium driver install uiautomator2
appium driver install xcuitest  # For iOS (coming soon)
```

## Project Structure

```
├── tests/
│   ├── mobile/
│   │   ├── pages/         # Page objects
│   │   ├── utils/         # Utility functions
│   │   └── test_*.py      # Test files
│   └── conftest.py        # Pytest fixtures and configuration
├── apps/                  # Mobile apps for testing
├── requirements.txt       # Python dependencies
└── pytest.ini            # Pytest configuration
```

## Configuration

The framework uses environment variables for configuration. Copy `.env.example` to `.env` and adjust the values:

```bash
cp .env.example .env
```

Key configurations:
- `APPIUM_HOST`: Appium server host
- `APPIUM_PORT`: Appium server port
- `PLATFORM_NAME`: Target platform (Android/iOS)
- `DEVICE_NAME`: Target device name
- `PLATFORM_VERSION`: OS version

## Running Tests

1. Start the Appium server:
```bash
appium
```

2. Start an Android emulator:
```bash
# Start the Pixel 7 API 35 emulator in read-only mode
emulator -avd Pixel_7_API_35 -read-only &
```

3. Run the tests:
```bash
# Run all tests
pytest tests/mobile -v

# Run specific test file
pytest tests/mobile/test_api_demos.py -v

# Run with specific marker
pytest -m android -v
```

## Android Testing

Currently supported features:
- Basic app launch and navigation
- Element interactions (tap, click, send keys)
- Screen verification
- Back navigation
- Screenshot capture

## iOS Testing (Coming Soon)

iOS support is under development. Features will include:
- XCUITest driver integration
- iOS simulator support
- iOS-specific element locators
- iOS app installation and launch
- iOS gesture support

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.