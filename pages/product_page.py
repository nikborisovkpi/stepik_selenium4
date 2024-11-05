from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_product_name(self):
        pr_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        bas_name = self.browser.find_element(*ProductPageLocators.BASKET_NAME)
        assert pr_name.text == bas_name.text,\
            "Selected product was not added to basket"

    def check_product_price(self):
        pr_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        bas_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert pr_price.text == bas_price.text, \
            "Basket price is not equal selected product price"


    def check_price_at_all(self):
        self.check_product_name()
        self.check_product_price()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should have disappeared"