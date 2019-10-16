from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOKS_NAME_IN_BASKET = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]")
    BOOKS_NAME = (By.XPATH, "//div[@class ='col-sm-6 product_main']/h1")
    BOOKS_PRICE_IN_BASKET =(By.CSS_SELECTOR, "div.alert-info strong")
    BOOKS_PRICE =(By.CSS_SELECTOR, "p.price_color")