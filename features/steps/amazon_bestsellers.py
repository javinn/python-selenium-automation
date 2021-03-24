from behave import given, when, then
from selenium.webdriver.common.by import By
# from time import sleep

# Homework 4-1

TAB_LINKS = (By.CSS_SELECTOR, 'div#zg_header li')
BEST_SELL = (By.XPATH, "//a[@href = 'https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab']")


@then("Verify number of links is 5")
def links_number(context):
    assert len(context.chrome_instance.find_elements(*TAB_LINKS)) == 5, 'Error! Number of links is NOT 5'


@then("Click on Bestsellers")
def step_impl(context):
    assert 'Best Sellers' == context.chrome_instance.find_element(*BEST_SELL).text


# Homework 6-2

HEADER_TEXT = (By.ID, 'zg_banner_text_wrapper')
TAB_LINK = (By.CSS_SELECTOR, 'div#zg_header a')


@then("User verifies each page")
def step_impl(context):
    tab_length = len(context.chrome_instance.find_elements(*TAB_LINK))
    for i in range(tab_length):
        context.chrome_instance.find_elements(*TAB_LINK)[i].click()
        assert context.chrome_instance.find_elements(*TAB_LINK)[i].text in context.chrome_instance.find_element(*HEADER_TEXT).text