from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form')
    BASKET_PRICE = (By.CSS_SELECTOR,'div[id="messages"]>div>div>p>strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main>p.price_color')
    BASKET_BOOK_NAME = (By.CSS_SELECTOR, 'div.alert.alert-safe.alert-noicon:first-child>div>strong')
    BOOK_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main>h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert.alert-safe.alert-noicon:first-child')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')

