from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_should_be_added_to_cart(self):
        self.prise_added_to_basket()
        self.product_added_to_cart()

    def add_product_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.add_button)
        add_button.click()

    def product_added_to_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.product_name).text
        message_text = self.browser.find_element(*ProductPageLocators.message).text
        assert product_name in message_text, 'Product name is wrong'

    def prise_added_to_basket(self):
        product_prise = self.browser.find_element(*ProductPageLocators.product_prise).text
        message_text = self.browser.find_element(*ProductPageLocators.message).text
        assert product_prise in message_text, 'Product prise and basket sum are not equal'
