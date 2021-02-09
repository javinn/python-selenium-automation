# Homework 4-3

from behave import given, then, step
from selenium.webdriver.common.by import By


GREETING = (By.CSS_SELECTOR, 'div.ss-landing-container')
CENTER_TOPICS = (By.CSS_SELECTOR, 'div.ss-rich-card-row')
SEARCH_FIELD = (By.ID, 'helpsearch')
BROWSE_TOPICS = (By.CSS_SELECTOR, 'div.a-spacing-small h1')
CATEGORY_SECTION = (By.CSS_SELECTOR, 'ul#category-section')
WRENCHES_IMAGE = (By.CSS_SELECTOR, 'div#help-gateway-category-0 img.csg-hb-promo')


@given("Open Amazon Customer Service")
def open_amazon_customer_service(context):
    context.chrome_instance.get('https://www.amazon.com/gp/help/customer/display.html')


@then("User checks greeting message")
def user_checks_greeting(context):
    context.chrome_instance.find_element(*GREETING)



@step("User checks center topics")
def check_center_topics(context):
    assert len(context.chrome_instance.find_elements(*CENTER_TOPICS)) == 3, 'Missing Topics in the Center Block!'


@step("User checks search field")
def user_checks_search(context):
    context.chrome_instance.find_element(*SEARCH_FIELD)


@step("User checks browse topics")
def user_checks_browse(context):
    context.chrome_instance.find_element(*BROWSE_TOPICS)


@step("User checks category section")
def check_category_section(context):
    context.chrome_instance.find_element(*CATEGORY_SECTION)


@step("User checks Wrenches image")
def check_wrenches(context):
    context.chrome_instance.find_element(*WRENCHES_IMAGE)



# Homework 4-4

def digitize(n):
    result = []
    while n != 0:
        result.append(n%10)
        n //= 10
    return result

