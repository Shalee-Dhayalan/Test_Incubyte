from behave import when, then
from pages.accountPasswordCharacters import AccountPage

@when("the user enters the following passwords:")
def step_enter_passwords(context):
    context.password_results = []
    for row in context.table:
        password = row["Password"]
        result = context.page.check_password_strength(password)
        context.password_results.append(result)

@then("the system should validate each password")
def step_validate_passwords(context):
    for result in context.password_results:
        print(result)