import time

import allure

from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from pages.specific_product_page import SpecificProductPage
from tests.test_base import TestBase


class TestCart(TestBase):

    @allure.description("checking default elements are displayed")
    def test_elements_displayed(self, login):
        p_products = ProductsPage(self.driver)
        p_cart = CartPage(self.driver)
        p_products.go_to_cart()
        p_cart.check_default_elements_displayed()

    @allure.description("checking 'continute shopping' button redirects to main products page")
    def test_continue_shopping_button(self):
        p_products = ProductsPage(self.driver)
        p_cart = CartPage(self.driver)
        p_cart.click_continue_shopping_button()
        products = p_products.products_list()
        assert len(products) > 1, ("List of products is not bigger than 1, is it products page?")

    @allure.description("testing items description is equal on cart page and products main page / specific page")
    def test_equal_items_data(self):
        p_products = ProductsPage(self.driver)
        p_specific = SpecificProductPage(self.driver)
        p_cart = CartPage(self.driver)
        p_products.reset_cart()
        p_products.add_remove_item_to_cart(0)
        product_in_products = p_products.get_specific_product(0).text
        print(product_in_products)
        p_products.enter_product_page(1)
        time.sleep(1)
        p_specific.click_add_remove_to_cart_btn()
        product_spec_text = p_specific.get_product().text
        print(product_spec_text)
        badge = p_products.check_cart_badge()
        assert badge == "2"
        p_products.go_to_cart()
        badge = p_products.check_cart_badge()
        assert badge == "2"
        prod_from_prods_text = p_cart.get_product_description(0)
        assert prod_from_prods_text == product_in_products, "There's a product data difference on cart compared to its' products page"
        prod_from_specific_page_text = p_cart.get_product_description(1)
        assert prod_from_specific_page_text == product_spec_text, "There's a product data difference on cart compared to its' specific page"

    @allure.description("no change in cart products when moving between pages")
    def test_same_cart_when_moving_between_pages(self):
        p_products = ProductsPage(self.driver)
        # p_specific = SpecificProductPage(self.driver)
        p_cart = CartPage(self.driver)
        list_of_prods1 = p_cart.get_list_of_products()
        p_cart.click_continue_shopping_button()
        p_products.go_to_cart()
        list_of_prods2 = p_cart.get_list_of_products()
        assert len(list_of_prods1) == len(list_of_prods2) , "when moving between pages amounts of items in cart is disrupted"
        p_cart.click_continue_shopping_button()
        p_products.get_specific_product(3)
        p_products.go_to_cart()
        list_of_prods3 = p_cart.get_list_of_products()
        assert len(list_of_prods1) == len(list_of_prods3) , "when moving between pages amounts of items in cart is disrupted"


    @allure.description("removing item from cart")
    def test_remove_item(self):
        p_cart = CartPage(self.driver)
        p_cart.remove_product(1)
        list_of_prods = p_cart.get_list_of_products()
        assert len(list_of_prods) == 1, "item was not removed"


