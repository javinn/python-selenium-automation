#  Homework 3-3

from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


SHOPPING_CART = (By.ID, 'nav-cart-count-container')
CART_STATUS = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty h2')

@given('Open Amazon Main page')
def open_amazon_page(context):
    context.chrome_instance.get('https://www.amazon.com/')


@when('Click on Shopping Cart')
def click_shopping_cart(context):
    context.chrome_instance.find_element(*SHOPPING_CART).click()
    sleep(4)

@then('Verify Shopping Cart is empty')
def verify_cart_status(context):
    assert 'Your Amazon Cart is empty' in context.chrome_instance.find_element(*CART_STATUS).text, 'Cart is not empty!!!'


