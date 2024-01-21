import time

from selenium import webdriver

from pages.loginPage import LoginPage


class TestsOfLogins:
    # running all kinds of tests logins:

    # global p_login
    def test_invalid_login(self):
        p_login = LoginPage(self.driver)
        p_login.login("no_user", "no_pass")
        error = p_login.error_message()
        assert "Username and password do not match" in error, "check error message"

    def test_valid_login(self):
        p_login = LoginPage(self.driver)
        p_login.login("standard_user", "secret_sauce")


