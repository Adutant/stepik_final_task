from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_ADDED_TO_BASKET_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE_MESSAGE = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")
    PRODUCT_NAME = (By.XPATH, "//article[@class='product_page']//h1")
    PRODUCT_PRICE = (By.XPATH, "//article[@class='product_page']//p[@class='price_color']")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@class='alert-success'][1]")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")