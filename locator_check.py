from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""
Homework 2-2

(By.XPATH, '//i [@class = "a-icon a-icon-logo"]')                                          - Amazon Logo

(By.ID, 'continue')                                                                         - Continue button

(By.XPATH, '//span[@class="a-expander-prompt"]')                                            - Need help link

(By.ID, "auth-fpp-link-bottom")                                                             - Forgot your password link

(By.ID, "ap-other-signin-issues-link")                                                      - Other issues with Sign-In link

(By.ID, "createAccountSubmit")                                                              - Create your Amazon account button

(By.XPATH, '//div[@id = "legalTextRow" ]//a[contains(text(), "Conditions of Use")]')        - Conditions of use link

(By.XPATH, '//div[@id = "legalTextRow" ]//a[contains(text(), "Privacy Notice")]')           - Privacy Notice link


"""
"""
Homework 3-1

It would be probably more optimal (faster) if CSS selectors of the type input# replace with By.ID   

(By.CSS_SELECTOR, 'i.a-icon-logo')                                                                                  - Amazon Logo
(By.CSS_SELECTOR, 'h1.a-spacing-small')                                                                             - Create account
(By.CSS_SELECTOR, 'input#ap_customer_name')                                                                         - Your name
(By.CSS_SELECTOR, 'input#ap_email')                                                                                 - Email
(By.CSS_SELECTOR, 'input#ap_password')                                                                              - Password
(By.CSS_SELECTOR, 'div.auth-inlined-information-message')                                                           - Password restriction
(By.CSS_SELECTOR, 'input#ap_password_check')                                                                        - Re-enter Password
(By.CSS_SELECTOR, 'input#continue')                                                                                 - Create your Amazon account
(By.XPATH, "//a[contains(@href,'ap_register_notification_condition_of_use')]")                                      - Conditions of Use
(By.XPATH, "//a[contains(@href,'ap_register_notification_privacy_notice')]")                                        - Privacy Notice
(By.CSS_SELECTOR, 'a.a-link-emphasis')                                                                              - Sign-in

"""
chrome_instance = webdriver.Chrome()

chrome_instance.implicitly_wait(4)

chrome_instance.get(
    'https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

chrome_instance.maximize_window()

# chrome_instance.find_element(By.XPATH, '//i [contains(@class, "a-icon-logo")]')
# sleep(4)
#
#
# continue_button = chrome_instance.find_element(By.ID, 'continue')
# continue_button.click()
# sleep(4)

# need_help_link = chrome_instance.find_element(By.XPATH, '//span[@class="a-expander-prompt"]')
# need_help_link.click()
# sleep(4)



# forgot_your_password_link = chrome_instance.find_element(By.ID, 'auth-fpp-link-bottom')
# forgot_your_password_link.click()
# sleep(4)


# other_issues_with_signin_link = chrome_instance.find_element(By.ID, 'ap-other-signin-issues-link')
# other_issues_with_signin_link.click()
# sleep(4)


# create_your_amazon_account_button = chrome_instance.find_element(By.ID, 'createAccountSubmit')
# create_your_amazon_account_button.click()
# sleep(4)


# conditions_of_use_link = chrome_instance.find_element(By.XPATH, '//div[@id = "legalTextRow" ]//a[contains(text(), "Privacy Notice")]')
# conditions_of_use_link.click()
# sleep(4)

# privacy_notice = chrome_instance.find_element(By.XPATH, "//a[contains(@href,'ap_register_notification_privacy_notice')]")
# privacy_notice.click()
# sleep(4)

input_check = chrome_instance.find_element(By.CSS_SELECTOR, 'input#ap_email')
input_check.send_keys('blablabla', Keys.ENTER)
sleep(4)



chrome_instance.quit()
