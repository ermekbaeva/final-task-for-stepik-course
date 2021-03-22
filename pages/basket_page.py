from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY_MESSAGE), 'Basket is not empty'