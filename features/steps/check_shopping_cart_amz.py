#  Homework 3-3

from behave import given, when, then
from selenium.webdriver.common.by import By
# from time import sleep


SHOPPING_CART = (By.ID, 'nav-cart-count-container')
CART_STATUS = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty h2')


@given('Open Amazon Main page')
def open_amazon_page(context):
    context.chrome_instance.get('https://www.amazon.com/')


@when('Click on Shopping Cart')
def click_shopping_cart(context):
    context.chrome_instance.implicitly_wait(4)
    context.chrome_instance.find_element(*SHOPPING_CART).click()
    # sleep(4)

@then('Verify Shopping Cart is empty')
def verify_cart_status_empty(context):
    assert 'Your Amazon Cart is empty' in context.chrome_instance.find_element(*CART_STATUS).text, 'Cart is not empty!!!'



#  Homework 3-4


BESTSELLERS = (By.XPATH, '//div[@id="nav-xshop"]/a[contains(@href, "bestsellers")]')
BESTSELLER_BOOKS = (By.XPATH, '//ul[@id="zg_browseRoot"]//a[contains(@href, "best-sellers-books")]')
TOP_BESTSELLER = (By.CSS_SELECTOR, 'ol#zg-ordered-list span.p13n-sc-price')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
CART_ITEM = (By.CSS_SELECTOR, 'div.a-row.a-spacing-base.a-spacing-top-base')


@when('User opens Bestsellers')
def open_bestsellers(context):
    context.chrome_instance.implicitly_wait(2)
    context.chrome_instance.find_element(*BESTSELLERS).click()
    # sleep(2)

@when('User opens Bestseller Books')
def open_bestseller_books(context):
    context.chrome_instance.implicitly_wait(2)
    context.chrome_instance.find_element(*BESTSELLER_BOOKS).click()
    # sleep(2)

@when('User opens the Top Bestseller')
def open_top_bestseller(context):
    context.chrome_instance.implicitly_wait(2)
    context.chrome_instance.find_elements(*TOP_BESTSELLER)[0].click()
    # sleep(2)

@when('User adds to Cart')
def add_to_cart(context):
    context.chrome_instance.implicitly_wait(2)
    context.chrome_instance.find_element(*ADD_TO_CART).click()
    # sleep(2)

@then('Verify Shopping Cart has exact {number} Item(s)')
def verify_number_of_items(context, number):
    number_of_cart_items = len(context.chrome_instance.find_elements(*CART_ITEM))
    assert number_of_cart_items == int(number), f'{number_of_cart_items} item(s) in cart. Expected {number} item(s)!!!'

