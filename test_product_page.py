from .pages.product_page import ProductPage
#product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
import time

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    #time.sleep(5)
    page.check_books_name_in_basket()
    page.check_books_price_in_basket()

    ###