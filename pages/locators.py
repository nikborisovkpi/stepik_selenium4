from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = ()
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE =(By.CSS_SELECTOR, ".product_main p.price_color")

    BASKET_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")