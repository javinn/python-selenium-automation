#  Homework 2-4

from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

ORDERS_BUTTON = (By.ID, 'nav-orders')
SIGNIN_TEXT = (By.XPATH, "//div[@class='a-box-inner a-padding-extra-large']/h1")


@given('Open Amazon page')
def open_amazon(context):
    context.chrome_instance.get('https://www.amazon.com/')
    sleep(4)


@when('Click on Returns&Orders Button')
def click_orders(context):
    context.chrome_instance.find_element(*ORDERS_BUTTON).click()
    sleep(4)


@then('Sign-in Page is Opened')
def verify_signin_page(context):
    assert 'Sign-In' in context.chrome_instance.find_element(*SIGNIN_TEXT).text
