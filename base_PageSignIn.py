from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePageSignIn:
    def open_url(self, url):
        self.sign_in_link = (By.XPATH, "(//div[@class='panel header']/ul/li)[2]")
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "pass")
        self.login_button = (By.CSS_SELECTOR, "#send2")

    def click_element(self, by, locator):
        element = self.find_element(by, locator)
        element.click()

    def enter_text(self, by, locator, text):
        element = self.find_element(by, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator))).text

    def is_element_displayed(self, by, locator):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((by, locator))).is_displayed()
        except:
            return False

    def get_current_url(self):
        return self.driver.current_url
