from .base_page import BasePage
from .locators import ProductPageLocators

from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_to_basket_button.click()

    def check_books_name_in_basket(self):
        book_in_basket = self.browser.find_element(*ProductPageLocators.BOOKS_NAME_IN_BASKET)
        books_name_in_basket = book_in_basket.text
        book = self.browser.find_element(*ProductPageLocators.BOOKS_NAME)
        books_name = book.text
        if books_name_in_basket == books_name:
            print("name is correct")
            assert True
        else:
            print("Need recheck the Name of book!!!")
            assert False
        #assert books_name.find(books_name_in_basket), "False again((("
        #print("Check books name: '" + books_name_in_basket + "' INCLUDE '" + books_name + "'")

    def check_books_price_in_basket(self):
        books_price_in_basket = self.browser.find_element(*ProductPageLocators.BOOKS_PRICE_IN_BASKET).text
        #books_name_in_basket = book_in_basket.text
        books_price = self.browser.find_element(*ProductPageLocators.BOOKS_PRICE).text
        #books_name = book.text
        if books_price_in_basket == books_price:
            print("price is correct")
            assert True
        else:
            print("Need recheck the price!!!")
            assert False
        #assert books_name.find(books_name_in_basket), "False again((("
        #print(books_name_in_basket + " and " + books_name)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disapeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be disappeared"


        #


