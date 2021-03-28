from pages.main_page import MainPage
from pages.bestsellers import Bestsellers


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.bestsellers = Bestsellers(self.driver)
