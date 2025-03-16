from behave import when, then
from pages.accountPasswordLength_page import AccountPage

@when('the user sets password "{password}" and confirms "{confirm_password}"')
def step_enter_passwords(context, password, confirm_password):
    context.page.enter_passwords(password, confirm_password)

@when("the user submits the registration form")
def step_submit_registration(context):
    context.page.submit_registration()

@then("the account should be created successfully")
def step_verify_account_creation(context):
    assert "Thank you for registering" in context.driver.page_source, "Account creation failed!"
