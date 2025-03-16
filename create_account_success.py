from behave import when, then
from pages.account_page_success import AccountPage

@given("the user is on the Magento Create Account page")
def step_open_create_account_page(context):
    context.page = AccountPage(context.driver)
    context.page.open_create_account_page()

@when('the user enters personal details')
def step_enter_user_details(context):
    for row in context.table:
        context.page.enter_user_details(row["First Name"], row["Last Name"], row["Email"])

@when('the user sets password "{password}" and confirms "{confirm_password}"')
def step_enter_passwords(context, password, confirm_password):
    context.page.enter_passwords(password, confirm_password)

@when("the user submits the registration form")
def step_submit_registration(context):
    context.page.submit_registration()

@then("the account should be created successfully")
def step_verify_account_creation(context):
    assert "Thank you for registering" in context.driver.page_source, "Account creation failed!"