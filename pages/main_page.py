from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage
from utilities.logger_config import logger


class MainPage(BasePage):
    MAIN_PAGE_CLOSE_BANNER = (By.XPATH, "//span[@class='close_btn line_close close_sub closeSub']")
    CLOSE_BANNER_PRODUCT_PAGE = (By.XPATH, "//i[@class='sz_custom_close']")
    CATEGORIES = (By.XPATH, "//span[@class='shop_cate_titles']")
    E_BIKE_OUTDOORS = (By.XPATH, "//a[contains(normalize-space(text()), 'E-Bikes & Outdoors')]")
    ENGWE_BIKE = (By.XPATH, "//li[@id='1170']")
    MIN_PRICE = (By.XPATH, "//input[@id='minPrice']")
    MAX_PRICE = (By.XPATH, "//input[@id='maxPrice']")
    FILTER_GO = (By.XPATH, "//input[@id='filterGo']")

    def close_main_page_banner(self):
        """
        Close the banner on the main page.
        """
        self.close_banner_if_present(self.MAIN_PAGE_CLOSE_BANNER)

    def close_banner_product_page(self):
        self.close_banner_if_present(self.CLOSE_BANNER_PRODUCT_PAGE)

    def get_categories(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.CATEGORIES))

    def get_e_bike_outdoors(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.E_BIKE_OUTDOORS))

    def get_engwe_bike(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.ENGWE_BIKE))

    def get_min_price(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.MIN_PRICE))

    def get_max_price(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.MAX_PRICE))

    def get_filter_go(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.FILTER_GO))

    def categories(self):
        self.get_categories().click()
        logger.info('Click categories')

    def e_bike_outdoors(self):
        self.get_e_bike_outdoors().click()
        logger.info('Click e_bike outdoors')

    def engwe_bike_brand(self):
        self.get_engwe_bike().click()
        logger.info('Click engwe bike brand')

    def min_price(self, min_price):
        self.get_min_price().send_keys(min_price)
        logger.info(f'input min price = {min_price}')

    def max_price(self, max_price):
        self.get_max_price().send_keys(max_price)
        logger.info(f'input min price = {max_price}')

    def filter_go(self):
        self.get_filter_go().click()
        logger.info('Click apply button')
