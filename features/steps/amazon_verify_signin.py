#  Homework 2-4

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ORDERS_BUTTON = (By.ID, 'nav-orders')
SIGNIN_TEXT = (By.XPATH, "//div[@class='a-box-inner a-padding-extra-large']/h1")


@given('Open Amazon page')
def open_amazon(context):
    context.chrome_instance.wait = WebDriverWait(context.chrome_instance, 10)
    context.chrome_instance.get('https://www.amazon.com/')
    context.chrome_instance.wait.until(EC.url_contains('https://www.amazon.com/'))

@when('Click on Returns&Orders Button')
def click_orders(context):
    context.chrome_instance.implicitly_wait(4)
    context.chrome_instance.find_element(*ORDERS_BUTTON).click()


@then('Sign-in Page is Opened')
def verify_signin_page(context):
    assert 'Sign-In' in context.chrome_instance.find_element(*SIGNIN_TEXT).text
