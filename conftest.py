import pytest
import os
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.logger_config import logger
from utilities.webdriver_proxy import WebDriverProxy
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def setup(request):
    logger.info("Запуск браузера")

    # Using ChromeDriverManager to automatically install the driver
    driver_path = ChromeDriverManager().install()
    logger.info(f"Используется драйвер: {driver_path}")

    # Setting up a service for the driver
    options = Options()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    # Wrapping WebDriver in a proxy class
    proxy_driver = WebDriverProxy(driver)

    # Browser settings
    proxy_driver.get("https://www.geekbuying.com/")
    proxy_driver.maximize_window()

    # Passing the proxy driver to the test class
    request.cls.driver = proxy_driver

    yield proxy_driver  # Returning the wrapped driver

    # Closing the browser
    proxy_driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook for checking test status. Takes a screenshot if the test fails.
    """
    outcome = yield
    report = outcome.get_result()

    #  Checking that the test crashed during execution
    if report.when == "call" and report.failed:
        # We are looking for a driver if it is in the test class
        driver = getattr(item.instance, "driver", None)
        if driver:
            # Create a directory for screenshots
            screenshots_dir = "screenshots"
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)

            # Forming a file name
            test_name = item.name
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"{test_name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, screenshot_name)

            # Taking a screenshot
            driver.save_screenshot(file_path)
            logger.error(f"Screenshot taken: {file_path}")
