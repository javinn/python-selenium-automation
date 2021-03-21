# Homework 2-3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from time import sleep

chrome_instance = webdriver.Chrome()

chrome_instance.get('https://www.amazon.com/gp/help/customer/display.html')

chrome_instance.maximize_window()

# sleep(4)
chrome_instance.implicitly_wait(4)

search_help_library_field = chrome_instance.find_element(By.ID, 'helpsearch')
search_help_library_field.send_keys('Cancel order', Keys.ENTER)

# sleep(4)

expected_text = "Cancel Items or Orders"

actual_text = chrome_instance.find_element(By.XPATH, '//div[@class="help-content"]/h1').text

assert expected_text in actual_text, f'expected "{expected_text}" but got "{actual_text}"'


chrome_instance.quit()