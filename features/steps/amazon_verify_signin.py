#  Homework 2-4
#  Homework 7-1

from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()

@when('Click on Returns&Orders Button')
def click_orders(context):
    context.app.main_page.click_orders()


@then('Sign-in Page is Opened')
def verify_signin_page(context):
    context.app.main_page.verify_signin_page()