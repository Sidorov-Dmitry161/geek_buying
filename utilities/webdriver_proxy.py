from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
from utilities.logger_config import logger, WebDriverResponseHandler


class WebDriverProxy:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def __getattr__(self, name):
        """
        Intercepts WebDriver attribute calls and wraps them in response processing
        """
        original_attr = getattr(self.driver, name)

        if callable(original_attr):
            def wrapper(*args, **kwargs):
                try:
                    #  Calling the original method
                    response = original_attr(*args, **kwargs)

                    if isinstance(response, dict):
                        WebDriverResponseHandler.check_response(response)

                    return response
                except WebDriverException as e:
                    raise e

            return wrapper
        return original_attr
