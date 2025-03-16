from basepage import BasePage
from selenium.webdriver.common.by import By
import pages.base_pageSignIn

from tests.pages.base_PageSignIn import BasePageSignIn


class LoginPage(BasePageSignIn):
    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard_url = "https://magento.softwaretestingboard.com/"

    def open_login_page(self):
        self.click_element(*self.sign_in_link)

    def enter_credentials(self, email, password):
        self.enter_text(*self.email_input, email)
        self.enter_text(*self.password_input, password)

    def submit_login(self):
        self.click_element(*self.login_button)

    def is_login_successful(self):
        return self.get_current_url() == self.dashboard_url