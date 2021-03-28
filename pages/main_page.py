#  Homework 7-1
#  Homework 7-2

from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):

  SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
  SEARCH_ICON = (By.ID, 'nav-search-submit-button')
  ORDERS_BUTTON = (By.ID, 'nav-orders')
  SIGNIN_TEXT = (By.CSS_SELECTOR, 'h1.a-spacing-small')
  SHOPPING_CART = (By.ID, 'nav-cart-count')
  CART_STATUS = (By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty h2')
  BESTSELLERS = (By.XPATH, '//div[@id="nav-xshop"]/a[contains(@href, "bestsellers")]')

  def open_main_page(self):
    self.open_page('https://www.amazon.com/')

  def input_amazon_search(self, search_query):
    self.input_text(search_query, *self.SEARCH_FIELD)

  def click_search_icon(self):
    self.click(*self.SEARCH_ICON)

  def click_orders(self):
    self.click(*self.ORDERS_BUTTON)

  def verify_signin_page(self):
    self.verify_text_is_in('Sign-In', *self.SIGNIN_TEXT)

  def click_shopping_cart(self):
    self.click(*self.SHOPPING_CART)

  def verify_cart_status_empty(self):
    self.verify_text_is_in('Your Amazon Cart is empty', *self.CART_STATUS)

  def open_bestsellers(self):
    self.click(*self.BESTSELLERS)