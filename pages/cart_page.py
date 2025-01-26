import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage
from utilities.logger_config import logger


class CartPage(BasePage):
    CART_TOTAL_PRICE = (By.XPATH, "//span[@id='lbGrandtotal2017']")

    def get_cart_total_price(self):

        try:
            total_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.CART_TOTAL_PRICE)
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", total_element)
            time.sleep(1)

            WebDriverWait(self.driver, 20).until(
                EC.visibility_of(total_element)
            )

            total_text = total_element.text.strip()
            logger.info(f"Received amount in cart: {total_text}")

            return float(total_text.replace('$', '').replace(',', ''))

        except Exception as e:
            logger.error(f"Error when receiving cart amount: {e}")
            return 0.0
