from basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pages.base_page

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.password_input = (By.XPATH, "//input[@id='password']")
        self.password_confirm_input = (By.ID,"password-confirmation")
        self.create_account_button = (By.XPATH, "//button[@title='Create an Account']")
        self.success_message = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")

    def enter_passwords(self, password, confirm_password):
        self.enter_text(*self.password_input, password)
        self.enter_text(*self.password_confirm_input, confirm_password)

    def submit_registration(self):
        self.click_element(*self.create_account_button)

    def success_message_validation(self):
        return self.get_text_message(*self.success_message)

