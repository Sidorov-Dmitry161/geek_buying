from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.logger_config import logger
from items import ITEM_LOCATORS

from base.base_page import BasePage


class ProductPage(BasePage):
    BIKE_LOCATOR = (By.XPATH, "//img[@alt='ENGWE M20 Electric Bike 20 Inch 48V 13AH 750W Motor45Km/h Speed Green']")
    ADD_TO_CART_BIKE = (By.XPATH, "//a[@onclick=\"geek_cart_drawer.addCart(1, 519824,1241,1794,2082,this)\"]")
    ADD_TO_CART_BTN = (By.XPATH, "//a[@class='cart_btn']")
    CYCLING = (By.XPATH, "//div[@id='content-sub']//a[normalize-space()='Cycling']")
    HEATING_GLOVES_LOCATOR = (By.XPATH, "//a[@id='518163']")
    ADD_TO_CART_GLOVES = (By.XPATH, "//a[@onclick='geek_cart_drawer.addCart(0, 518163,1241,1265,1790,this)']")
    LOCK_LOCATOR = (By.XPATH, "//a[@id='518203']")
    ADD_TO_CART_LOCK_BICYCLE = (By.XPATH, "//a[@onclick='geek_cart_drawer.addCart(1, 518203,1241,1265,1790,this)']")
    CART = (By.XPATH, "//div[@class='head_cart']")

    prices = {}

    def add_to_cart_hover_bike(self):
        self.hover_and_click(self.BIKE_LOCATOR, self.ADD_TO_CART_BIKE)

    def add_to_cart_hover_gloves(self):
        self.hover_and_click(self.HEATING_GLOVES_LOCATOR, self.ADD_TO_CART_GLOVES)

    def add_to_cart_hover_lock(self):
        self.hover_and_click(self.LOCK_LOCATOR, self.ADD_TO_CART_LOCK_BICYCLE)

    def add_to_cart_and_save_price(self, item_key, item_locator, add_button_locator):
        """
        Method for adding an item to the cart and saving its price.
        """
        try:
            # We save the price of the product until it is added to the cart
            price = self.get_price(item_key)
            self.prices[item_key] = price
            logger.info(f"Price item {item_key}: {price} saved.")

            # We wait for the product to appear and add it to the cart
            self.hover_and_click(item_locator, add_button_locator)
            logger.info(f"Item {item_key} add to cart.")

        except Exception as e:
            logger.error(f"Error adding product {item_key}: {e}")

    def get_add_to_cart_btn(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN))

    def get_cycling(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.CYCLING))

    def get_cart(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.CART))

    def add_to_cart(self):
        self.get_add_to_cart_btn().click()
        logger.info('Click Add to Cart')

    def cycling(self):
        self.get_cycling().click()
        logger.info('Click Cycling')

    def go_to_cart(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.get_cart().click()
        logger.info('Click Cart')

    def get_price(self, item_key):
        """
        Gets the price for the specified product using the item_key.
        """
        try:
            locator = ITEM_LOCATORS[item_key]
            logger.info(f"We are looking for a price for {item_key} with locator: {locator}")

            #  Waiting for an element with a price of DOM
            price_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(locator)
            )

            if price_element:
                price_text = price_element.text.strip()

                if not price_text:
                    logger.error(f"Item with price for {item_key} found, but text is empty.")
                    return 0.0

                logger.info(f"Found price text for {item_key}: {price_text}")
                print(f"Found price text for {item_key}: {price_text}")

                # Clear price text from symbols to leave only numbers
                price_text_cleaned = price_text.replace('$', '').strip()

                try:
                    price = float(price_text_cleaned)
                    print(f"Price for {item_key}: {price}")
                except ValueError:
                    logger.error(f"Error converting price text '{price_text_cleaned}' for {item_key}.")
                    return 0.0

                logger.info(f"Price for {item_key}: {price}")
                return price
            else:
                logger.error(f"Item with price for {item_key} not found.")
                return 0.0

        except Exception as e:
            logger.error(f"Error getting price for {item_key}: {e}")
            return 0.0

    def calculate_total_price(self, items):
        """
        Sums prices for a list of products.
        :param items: list of product keys.
        :return: total cost of goods.
        """
        total_price = 0.0
        for item in items:
            if item in self.prices:
                price = self.prices[item]
                logger.info(f"Added to total cost: {price} for item {item}")
                total_price += price
            else:
                logger.error(f"Product price {item} not found.")
                return 0.0

        logger.info(f"Total cost for items {items}: {total_price}")
        return total_price
