from os import link
from .pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"


def test_gust_can_add_to_cart(browser):
    page = ProductPage(browser, link)
    try:
        page.open()
        page.add_product_to_cart()
        # page.solve_quiz_and_get_code()
        page.product_should_be_added_to_cart()
    except Exception as e:
        pytest.fail(f"Произошла ошибка: {str(e)}")
    finally:
        print(f'Тест с сылкой {page.url} прошел успешно')


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_be_disappeared_message()
