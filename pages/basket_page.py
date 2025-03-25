from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_have_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EmptyBasketMessage), "Empty basket message isn't shown"
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EmptyBasketMessage)
        expected_text = empty_basket_message.text
        assert expected_text == "Your basket is empty. Continue shopping", \
            "Empty basket message text isn't the expected one"