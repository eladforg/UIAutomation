import time

import allure

from pages.products_page import ProductsPage
from pages.specific_product_page import SpecificProductPage
from tests.test_base import TestBase


class TestSpecificProductPage(TestBase):


    @allure.description("checking product data is equal on both products page and its' page")
    def test_equal_data(self, login):
        p_products = ProductsPage(self.driver)
        p_specific = SpecificProductPage(self.driver)
        product_in_products = p_products.get_product().text
        print(product_in_products)
        p_products.enter_product_page()
        time.sleep(1)
        # product_spec = p_specific.get_product().text
        product_spec = p_specific.get_item_description()
        print(product_spec)
        assert product_spec == product_in_products, "There's a product data difference on products page compared to its' specific page"

