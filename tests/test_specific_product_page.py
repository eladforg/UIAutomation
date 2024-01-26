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
        p_products.reset_cart()
        product_in_products = p_products.get_specific_product(2).text
        print(product_in_products)
        p_products.enter_product_page(2)
        time.sleep(1)
        # product_spec = p_specific.get_product().text
        product_spec = p_specific.get_item_description()
        print(product_spec)
        assert product_spec == product_in_products, "There's a product data difference on products page compared to its' specific page"


    @allure.description("Testing the cart badge")
    def test_cart_badge(self):
        p_products = ProductsPage(self.driver) #for the cart
        p_specific = SpecificProductPage(self.driver)
        p_specific.click_add_remove_to_cart_btn()
        time.sleep(1)
        badge = p_products.check_cart_badge()
        assert badge =="1"


    @allure.description("testing back to products page")
    def test_back_to_products_page(self):
        p_products = ProductsPage(self.driver)
        p_specific = SpecificProductPage(self.driver)
        p_products.back_to_products_page()
        products = p_products.products_list()
        assert len(products) > 1, ("List of products is not bigger than 1, is it products page?")
        badge = p_products.check_cart_badge()
        assert badge == "1"
        p_products.enter_product_page(1)
        time.sleep(1)
        badge = p_products.check_cart_badge()
        assert badge == "1"
        p_specific.click_back()
        products = p_products.products_list()
        # print(len(products))
        assert len(products) > 1, ("List of products is not bigger than 1, is it products page?")
        badge = p_products.check_cart_badge()
        assert badge == "1"


