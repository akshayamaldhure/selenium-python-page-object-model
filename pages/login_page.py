from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import *

from core.conf.environments.config import get_config_object


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        config = get_config_object()
        self.driver.get(config.AUTOMATION_PRACTICE_URL)

    email = (By.ID, EMAIL_ID)
    password = (By.ID, PASSWORD_ID)
    sign_in_btn = (By.ID, SIGN_IN_BTN_ID)
    failure_message = (By.XPATH, LOGIN_FAILURE_MESSAGE_XPATH)

    def set_email(self, email):
        email_element = self.driver.find_element(*LoginPage.email)
        email_element.clear()
        email_element.send_keys(email)

    def set_password(self, password):
        password_element = self.driver.find_element(*LoginPage.password)
        password_element.clear()
        password_element.send_keys(password)

    def click_sign_in_btn(self):
        sign_in_element = self.driver.find_element(*LoginPage.sign_in_btn)
        sign_in_element.click()

    def is_failure_message_displayed(self):
        failure_message_element = self.driver.find_element(*LoginPage.failure_message)
        return failure_message_element.is_displayed()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_btn()
