from .pages.product_page import ProductPage
import pytest
import time

# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.check_price_at_all()


@pytest.mark.parametrize('index', ["offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                   pytest.param("offer7", marks=pytest.mark.xfail), ])
def test_guest_can_add_product_to_basket(browser, index):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={index}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_price_at_all()