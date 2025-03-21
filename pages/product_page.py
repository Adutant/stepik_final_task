from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_message_product_add_to_basket_shown(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_added_to_basket_message = (
            self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE))
        assert product_name.text == product_added_to_basket_message.text, \
            "Product name in basket isn't the expected one"

    def should_be_message_product_price_shown(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MESSAGE)
        assert product_price.text == product_price_message.text, "Product price in basket isn't the expected one"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message isn't disappeared, but should"

