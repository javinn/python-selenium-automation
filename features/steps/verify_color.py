#  Homework 5-2

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ITEM_VARIATIONS = (By.CSS_SELECTOR, 'div#variation_color_name li')
ITEM_COLOR = (By.CSS_SELECTOR,'div#variation_color_name span.selection')


@given('Open Item Page of {product_no}')
def open_item_page(context, product_no):
    context.chrome_instance.get(f'https://www.amazon.com/gp/product/{product_no}/')


@then('Check all Colors')
def check_colors(context):
    context.chrome_instance.implicitly_wait(5)
    context.chrome_instance.wait = WebDriverWait(context.chrome_instance, 10)

    colors = ['Black', 'Blue Overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage', 'Light Wash',
              'Medium Vintage', 'Medium Wash', 'Rinse', 'Rinsed Vintage', 'Vintage Light Wash', 'Washed Black']
    item_variations = context.chrome_instance.find_elements(*ITEM_VARIATIONS)
    i = 0
    for item in item_variations:
        context.chrome_instance.wait.until(EC.element_to_be_clickable)
        item.click()
        item_color = context.chrome_instance.find_element(*ITEM_COLOR)
        assert item_color.text == colors[i], f'Color {item_color.text} is not available'
        i += 1