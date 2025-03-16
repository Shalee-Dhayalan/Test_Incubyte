from behave import given, when, then
from selenium import webdriver
from pages.signIn_success import LoginPage

@then("the user should see an error message")
def step_verify_error_message(context):
    error_message = context.page.get_error_message()
    assert error_message, "Expected an error message but none was displayed!"
    print(f"❌ Login failed with error: {error_message}")
    context.driver.quit()
