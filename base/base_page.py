import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    LOGIN_PAGE_CLOSE_BANNER = (By.XPATH, "//i[@class='sz_custom_close']")
    MAIN_PAGE_CLOSE_BANNER = (By.XPATH, "//span[@class='close_btn line_close close_sub closeSub']")

    def close_banner_if_present(self, banner_locator):
        """
        The method checks for the presence of an advertisement and closes it if it exists.
        """
        try:
            close_button = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(banner_locator)
            )
            close_button.click()
            print("Banner is closed")
        except TimeoutException:
            print("Banner not found. Let's continue the test.")

    def hover_and_click(self, element_locator, button_locator, timeout=20):
        """
        Scrolls to an element, moves the mouse over it and clicks on the button that appears.

        :param element_locator: Locator of the element to hover over.
        :param button_locator: Locator for a button that appears after hover.
        :param timeout: Maximum waiting time.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(element_locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            time.sleep(1)

            button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(button_locator)
            )

            try:
                button.click()
                print("Successfully clicked the button")
            except Exception as click_error:
                print(f"Standard click didn't work: {click_error}. Trying a JavaScript click.")
                self.driver.execute_script("arguments[0].click();", button)

        except Exception as e:
            print(f"Error when hovering, scrolling, or clicking a button: {e}")
