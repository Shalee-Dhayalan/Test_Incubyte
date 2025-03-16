from selenium.webdriver.common.by import By


class BasePage:
    def open_url(self, url):
        self.driver.get(url)

    def __init__(self, driver):
        self.driver = driver
        self.create_account_link = (By.XPATH, "(//div[@class='panel header']/ul/li)[3]")
        self.firstname_input = (By.ID, "firstname")
        self.lastname_input = (By.ID, "lastname")
        self.email_input = (By.ID, "email_address")

    def click_element(self, by, locator):
        element = self.find_element(by, locator)
        element.click()

    def enter_text(self, by, locator, text):
        element = self.find_element(by, locator)
        element.clear()
        element.send_keys(text)

    def open_create_account_page(self):
        self.click_element(*self.create_account_link)

    def enter_user_details(self, firstname, lastname, email):
        self.enter_text(*self.firstname_input, firstname)
        self.enter_text(*self.lastname_input, lastname)
        self.enter_text(*self.email_input, email)

    def get_text_message(self,by,locator):
        element = self.find_element(by, locator)
        validation_message = element.text
        print(validation_message)


