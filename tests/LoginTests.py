import lemoncheesecake.api as lcc
from lemoncheesecake.matching import check_that, is_true
from selenium import webdriver

from core.common.constants import Global
from core.utils.fileutils import capture_screenshot
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage


@lcc.suite("Login page tests")
class LoginTests(object):
    login, my_account, driver = None, None, None

    def setup_suite(self):
        lcc.log_info("Inside setup")
        self.driver = webdriver.Chrome(executable_path=Global.CHROME_DRIVER)
        self.login = LoginPage(driver=self.driver)
        self.my_account = MyAccountPage(driver=self.driver)

    @lcc.test("check login failure")
    def verify_login_failure(self):
        self.login.login(email="akshaymaldhure@gmail.com", password="admin123")
        check_that("Failure message is displayed", self.login.is_failure_message_displayed(), is_true())

    @lcc.test("check login success")
    def verify_login_success(self):
        self.login.login(email="akshaymaldhure@gmail.com", password="admin")
        check_that("My Account text is displayed", self.my_account.is_my_account_text_displayed(), is_true())

    def teardown_test(self, test_name):
        lcc.log_info("Finished running test " + test_name)
        capture_screenshot(self.driver)

    def teardown_suite(self):
        lcc.log_info("Inside teardown")
        self.driver.quit()
