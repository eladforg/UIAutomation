import time

import allure

from pages.loginPage import LoginPage
from pages.products_page import ProductsPage
from pages.specific_product_page import SpecificProductPage
from tests.test_base import TestBase


class TestsOfProductsPage(TestBase):

    @allure.description("checking price is displayed for every item")
    def test_products_data(self, login):
        # p_login = LoginPage(self.driver)
        # p_login.login("standard_user", "secret_sauce")
        p_products = ProductsPage(self.driver)
        products = p_products.products_list()
        for item in products:
            assert "$" in item.text, "it seems price is not displayed"



    @allure.description("add and remove items to cart and check cart badge number")
    def test_add_and_remove__item_to_cart(self, login):
        p_products = ProductsPage(self.driver)
        p_products.add_remove_item_to_cart(2)
        time.sleep(1)
        badge = p_products.check_cart_badge()
        assert badge=="1"
        p_products.add_remove_item_to_cart(3)
        time.sleep(1)
        badge = p_products.check_cart_badge()
        assert badge == "2"
        p_products.add_remove_item_to_cart(3)
        time.sleep(1)
        badge = p_products.check_cart_badge()
        assert badge == "1"