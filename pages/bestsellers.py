#  Homework 7-2

from pages.base_page import Page
from selenium.webdriver.common.by import By


class Bestsellers(Page):


    BESTSELLER_BOOKS = (By.XPATH, '//ul[@id="zg_browseRoot"]//a[contains(@href, "best-sellers-books")]')
    TOP_BESTSELLER = (By.CSS_SELECTOR, 'ol#zg-ordered-list span.p13n-sc-price')
    ADD_TO_CART = (By.ID, 'add-to-cart-button')
    CART_ITEM = (By.CSS_SELECTOR, 'span#nav-cart-count')

    def open_bestseller_books(self):
        self.click(*self.BESTSELLER_BOOKS)

    def open_top_bestseller(self):
        self.click(*self.TOP_BESTSELLER)

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def verify_number_of_items(self):
        self.verify_text_is_in('1', *self.CART_ITEM)