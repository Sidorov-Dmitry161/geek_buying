from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage
from utilities.logger_config import logger
import random
import string


class LoginPage(BasePage):
    REGISTER = (By.XPATH, "//span[@class='login_account']")
    INPUT_EMAIL = (By.XPATH, "//input[@id='loginEmail']")
    CONTINUE_BTN = (By.XPATH, "//input[@id='loginContinue']")
    PASSWORD = (By.XPATH, "//input[@id='singUpPassword']")
    AGREE_POLICY = (By.XPATH, "//input[@id='geekProtocol']")
    CREATE_ACCOUNT = (By.XPATH, "//input[@id='signupBtn']")
    CLOSE_BANNER = (By.XPATH, "//i[@class='sz_custom_close']")
    LOGIN_PAGE_CLOSE_BANNER = (By.XPATH, "//i[@class='sz_custom_close']")

    def get_register(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.REGISTER))

    def get_input_email(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.INPUT_EMAIL))

    def get_continue_btn(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.CONTINUE_BTN))

    def get_password(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.PASSWORD))

    def get_agree_policy(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.AGREE_POLICY))

    def get_create_account(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.CREATE_ACCOUNT))

    # Action
    def click_register_btn(self):
        self.get_register().click()
        logger.info('Click register button')

    def input_email(self):
        email = self.generate_random_email()
        self.get_input_email().send_keys(email)
        logger.info(f'Input email {email}')
        return email

    def click_continue_btn(self):
        self.get_continue_btn().click()
        logger.info('Click continue button')

    def input_password(self):
        password = self.generate_random_password()
        self.get_password().send_keys(password)
        logger.info(f"Input password: {password}")
        return password

    def agree_policy(self):
        self.get_agree_policy().click()
        logger.info('Click agree policy')

    def create_account_button(self):
        self.get_create_account().click()
        logger.info('Click create account')

    def close_login_page_banner(self):
        """
        Close the banner on the login page.
        """
        self.close_banner_if_present(self.LOGIN_PAGE_CLOSE_BANNER)

    @staticmethod
    def generate_random_name():
        random_username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        return f"{random_username}"

    @staticmethod
    def generate_random_email():
        domains = ["example.com", "test.com", "demo.com"]
        random_username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        random_domain = random.choice(domains)
        return f"{random_username}@{random_domain}"

    @staticmethod
    def generate_random_password():
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
        return ''.join(random.sample(password, len(password)))
