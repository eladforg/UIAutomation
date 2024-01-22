import time

import allure
from _pytest.fixtures import fixture
from selenium import webdriver

from pages.loginPage import LoginPage
from pages.products_page import ProductsPage
from tests.test_base import TestBase


class TestsOfLogins(TestBase):
    # running all kinds of tests logins:

    # global p_login

    @allure.description("invalid login")
    def test_invalid_login(self):
        p_login = LoginPage(self.driver)
        p_login.login("no_user", "no_pass")
        error = p_login.error_message()
        assert "Username and password do not match" in error, "check error message"

    @allure.description("valid login")
    def test_valid_login(self, login):
        # p_login = LoginPage(self.driver)
        # p_login.login("standard_user", "secret_sauce")
        p_products = ProductsPage(self.driver)
        products=p_products.check_products_displayed()
        assert products > 0, "Products are not displayed!"


