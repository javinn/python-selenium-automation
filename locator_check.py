from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Homework 2-2

Could you please answer the *questions* with explanations? Thank you!

(By.XPATH, '//i [@class = "a-icon a-icon-logo"]')           - Amazon Logo
(By.XPATH, '//i [contains(@class, "a-icon-logo")]')         - Amazon Logo
        *Which one of the locators above is more preferable?*


"""

chrome_instance = webdriver.Chrome()

chrome_instance.get(
    'https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

chrome_instance.maximize_window()

chrome_instance.find_element(By.XPATH, '//i [contains(@class, "a-icon-logo")]')

chrome_instance.quit()
