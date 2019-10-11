from .base_page import BasePage

class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element_by_css_selector("#login_link")
        link.click()

        ####