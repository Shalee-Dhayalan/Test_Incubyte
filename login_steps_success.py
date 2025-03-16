from behave import given, when, then
from selenium import webdriver
from pages.signIn_success import LoginPage

@given("the user is on the Magento login page")
def step_open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://magento.softwaretestingboard.com/")
    context.page = LoginPage(context.driver)
    context.page.open_login_page()

@when('the user enters email "{email}" and password "{password}"')
def step_enter_credentials(context, email, password):
    context.page.enter_credentials(email, password)

@when("clicks the login button")
def step_click_login(context):
    context.page.submit_login()

@then("the user should be successfully logged in")
def step_verify_login(context):
    assert context.page.is_login_successful(), "Login failed! Incorrect credentials."
    print("Successfully logged in with your account.")
    context.driver.quit()