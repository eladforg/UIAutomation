from selenium import webdriver

from pages.loginPage import LoginPage


class TestsOfLogins:


# running all kinds of tests logins:

    def test_valid_login(self):

        p_login = LoginPage(self.driver)
        p_login.login("standard_user", "secret_sauce")
