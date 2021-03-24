# Homework 6-1

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


AMAZON_APPLICATIONS = (By.XPATH, '//a[contains(@href, "gp/feature.html")]')
DOWNLOAD_APP = (By.ID, 'mgt-email-sms-download-header')


@given("Open Amazon T&C page")
def step_impl(context):
    context.chrome_instance.get("https://www.amazon.com/gp/help/customer/display.html/ref"
                                "=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when("Store original windows")
def step_impl(context):
    context.original_window = context.chrome_instance.current_window_handle


@when("Click on Amazon applications link")
def step_impl(context):
    context.chrome_instance.find_element(*AMAZON_APPLICATIONS).click()
    context.old_windows = context.chrome_instance.window_handles


@when("Switch to the newly opened window")
def step_impl(context):
    context.chrome_instance.wait = WebDriverWait(context.chrome_instance, 10)
    new_window = context.old_windows[1]
    context.chrome_instance.switch_to_window(new_window)


@then("Amazon app page is opened")
def step_impl(context):
    context.chrome_instance.wait.until(EC.new_window_is_opened)
    assert 'app' in context.chrome_instance.find_element(*DOWNLOAD_APP).text, f'ERROR! False page'


@then("User can close new window and switch back to original")
def step_impl(context):
    context.chrome_instance.close()
    context.chrome_instance.switch_to_window(context.original_window)