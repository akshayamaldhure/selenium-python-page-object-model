from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import *


class MyAccountPage(BasePage):
    my_account_text = (By.XPATH, MY_ACCOUNT_TEXT)

    def is_my_account_text_displayed(self):
        email_element = self.driver.find_element(*MyAccountPage.my_account_text)
        return email_element.is_displayed()
