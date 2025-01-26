import logging
from typing import Dict, Any
from selenium.common.exceptions import (
    WebDriverException, NoSuchElementException, TimeoutException
)
from selenium.webdriver.remote.errorhandler import ErrorCode

# Setting up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
selenium_logger.setLevel(logging.WARNING)


class WebDriverResponseHandler:
    """
    A class for checking and processing WebDriver JSON responses
    """

    @staticmethod
    def check_response(response: Dict[str, Any]) -> None:
        """
        Checks the WebDriver JSON response and throws an exception if there is an error.

        :param response: Reply from WebDriver
        """
        status = response.get('status', None)
        if not status or status == ErrorCode.SUCCESS:
            return  # The answer is successful, we do nothing

        value = response.get('value', {})
        message = value.get('message', 'Unknown WebDriver error occurred')

        # Logging the error
        logger.error(f"WebDriver Error: Status: {status}, Message: {message}")

        # Determining the type of exception
        exception_class = WebDriverException
        if status in ErrorCode.NO_SUCH_ELEMENT:
            exception_class = NoSuchElementException
        elif status in ErrorCode.TIMEOUT:
            exception_class = TimeoutException

        # Throwing an exception
        raise exception_class(message)
