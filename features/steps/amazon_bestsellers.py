from behave import given, when, then
from selenium.webdriver.common.by import By
# from time import sleep

# Homework 4-1

TAB_LINKS = (By.CSS_SELECTOR, 'div#zg_header li')
BEST_SELL = (By.XPATH, "//a[@href = 'https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab']")


@then("Verify number of links is 5")
def links_number(context):
    assert len(context.chrome_instance.find_elements(*TAB_LINKS)) == 5, 'Error! Number of links is NOT 5'


@step("Click on Bestsellers")
def step_impl(context):
   assert 'Best Sellers' == context.chrome_instance.find_element(*BEST_SELL).text