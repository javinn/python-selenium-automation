# Homework 3-2

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


SEARCH_HELP_FIELD = (By.ID, 'helpsearch')
ACTUAL_TEXT = (By.XPATH, '//div[@class="help-content"]/h1')

@given('Open Amazon Help page')
def open_amz_help(context):
    context.chrome_instance.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Input {topic} into Search Help field')
def input_search(context, topic):
    search_field = context.chrome_instance.find_element(*SEARCH_HELP_FIELD)
    search_field.clear()
    search_field.send_keys(topic)
    sleep(4)

@when('Click on Enter button')
def click_enter(context):
    context.chrome_instance.find_element(*SEARCH_HELP_FIELD).send_keys(Keys.ENTER)

@then('Verify {expected_text} is present')
def verify_text(context, expected_text):
    actual_text = context.chrome_instance.find_element(*ACTUAL_TEXT).text
    assert expected_text in actual_text, f'Error! Expected "{expected_text}", not "{actual_text}"'
