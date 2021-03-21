#  Homework 5-3

from selenium.webdriver.common.by import By
from behave import given, when, then

REGULAR = (By.CSS_SELECTOR,'ul.s-result-list.s-col-2 span.wfm-sales-item-card__regular-price')
PRODUCT_NAME = (By.CSS_SELECTOR, 'ul.s-result-list.s-col-2 li.s-result-item span.wfm-sales-item-card__product-name')

@given('Open Amazon Whole Foods page')
def open_whole_foods(context):
    context.chrome_instance.get('https://www.amazon.com/fmc/storedeals/?_encoding=UTF8&almBrandId=VUZHIFdob2xlIEZvb2Rz')


@then('Verify every product has Name')
def has_name(context):
    products_names = context.chrome_instance.find_elements(*PRODUCT_NAME)

    for product in products_names:
        assert len(product.text) > 0


@then('Verify every product has Regular')
def has_regular(context):
    products_regular = context.chrome_instance.find_elements(*REGULAR)

    for product in products_regular:
        assert 'Regular' in product.text