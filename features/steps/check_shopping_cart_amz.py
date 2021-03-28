#  Homework 3-3
#  Homework 7-1

from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon Main page')
def open_amazon_page(context):
    context.app.main_page.open_main_page()


@when('Click on Shopping Cart')
def click_shopping_cart(context):
    context.app.main_page.click_shopping_cart()

@then('Verify Shopping Cart is empty')
def verify_cart_status_empty(context):
    context.app.main_page.verify_cart_status_empty()


#  Homework 3-4
#  Homework 7-2


@when('User opens Bestsellers')
def open_bestsellers(context):
    context.app.main_page.open_bestsellers()

@when('User opens Bestseller Books')
def open_bestseller_books(context):
    context.app.bestsellers.open_bestseller_books()

@when('User opens the Top Bestseller')
def open_top_bestseller(context):
    context.app.bestsellers.open_top_bestseller()

@when('User adds to Cart')
def add_to_cart(context):
    context.app.bestsellers.add_to_cart()

@then('Verify Shopping Cart has exact one Item')
def verify_number_of_items(context):
    context.app.bestsellers.verify_number_of_items()

