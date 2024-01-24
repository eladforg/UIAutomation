import time

from _pytest.fixtures import fixture

from pages.loginPage import LoginPage
from pages.products_page import ProductsPage


class TestBase:

    @fixture
    def login(self):
        p_login = LoginPage(self.driver)
        p_login.login("standard_user", "secret_sauce")
        time.sleep(1)