from basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pages.base_page

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.password_input = (By.XPATH, "//input[@id='password']")
        self.password_confirm_input = (By.ID, "password-confirmation")
        self.create_account_button = (By.XPATH, "//button[@title='Create an Account']")
        self.password_error_message = (By.ID, "password-error")

    def validate_password(self, password):
        password_field = self.driver.find_element(*self.password_input)
        password_field.send_keys(password)
        password_field.send_keys(Keys.TAB)
        try:
            error_message = self.driver.find_element(*self.password_error_message)
            if error_message.is_displayed():
                return f"Password '{password}' failed validation: {error_message.text}"
            else:
                return f"Password '{password}' passed validation"
        finally:
            print("Password validation executed")

    def enter_passwords(self, password, confirm_password):
        self.enter_text(*self.password_input, password)
        self.enter_text(*self.password_confirm_input, confirm_password)

    def submit_registration(self):
        self.click_element(*self.create_account_button)