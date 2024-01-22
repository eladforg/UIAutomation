import time

from pages.loginPage import LoginPage
from pages.products_page import ProductsPage
from pages.specific_product_page import SpecificProductPage
from tests.test_base import TestBase


class TestsOfProductsPage(TestBase):

    def test_products_data(self, login):
        # p_login = LoginPage(self.driver)
        # p_login.login("standard_user", "secret_sauce")
        p_products = ProductsPage(self.driver)
        p_products.check_products_data()
        p_products.enter_product_page()
        time.sleep(5)
        p_item = SpecificProductPage(self.driver)
        p_item.click_back()
        p_products.check_products_data()
