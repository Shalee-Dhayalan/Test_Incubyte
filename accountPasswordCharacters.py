from basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pages.base_page

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.password_input = (By.XPATH, "//input[@id='password']")
        self.password_error_message = (By.ID, "password-error")

    def check_password_strength(self, password):
        """Enter a password and check its validation message"""
        password_field = self.driver.find_element(*self.password_input)
        password_field.clear()
        password_field.send_keys(password)
        password_field.send_keys(Keys.TAB)

        try:
            error_message = self.driver.find_element(*self.password_error_message)
            if error_message.is_displayed():
                return f"Password '{password}' failed validation: {error_message.text}"
            else:
                return f"Password '{password}' passed validation"
        except:
            return f"Password '{password}' passed validation (no error message displayed)"
        finally:
            print("Password validation executed")