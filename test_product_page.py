from pages.product_page import ProductPage
from pages.base_page import BasePage
import pytest
import time


@pytest.mark.parametrize('promo',
                         ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.basket_price_should_be_correct()
    page.book_name_in_basket_should_be_correct()
