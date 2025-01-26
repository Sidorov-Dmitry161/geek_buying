import time

import pytest

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from utilities.logger_config import logger


@pytest.mark.usefixtures("setup")
class TestSmoke:
    logger.info("Start test")

    def test_registration_new_user(self):
        # Registration new user
        main_page = MainPage(self.driver)
        main_page.close_main_page_banner()
        login_page = LoginPage(self.driver)
        login_page.click_register_btn()
        login_page.input_email()
        login_page.click_continue_btn()
        login_page.input_password()
        login_page.agree_policy()
        login_page.create_account_button()
        login_page.close_login_page_banner()
        # Choose items
        main_page.categories()
        main_page.e_bike_outdoors()
        main_page.close_banner_product_page()
        main_page.engwe_bike_brand()
        main_page.min_price(500)
        main_page.max_price(1000)
        main_page.filter_go()
        main_page.close_banner_product_page()
        time.sleep(1)
        # Adding items to cart
        product_page = ProductPage(self.driver)
        product_page.add_to_cart_hover_bike()
        product_page.add_to_cart()
        product_page.cycling()
        product_page.add_to_cart_hover_gloves()
        product_page.add_to_cart_hover_lock()
        product_page.add_to_cart()
        # Go to cart
        product_page.go_to_cart()
        cart_page = CartPage(self.driver)
        # List of products added to cart
        expected_total = product_page.calculate_total_price(["engwe_bike", "heating_gloves", "lock"])
        actual_total = cart_page.get_cart_total_price()
        print(f'Total price = {actual_total}')
        assert expected_total == actual_total, f"Expected amount {expected_total}, but received {actual_total}"
