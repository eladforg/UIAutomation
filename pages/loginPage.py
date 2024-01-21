import time

from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class LoginPage(BasePage):

    USER_NAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)


    def login(self, username, password):
        self.fill_text(self.USER_NAME, username)
        self.fill_text(self.PASSWORD, password)
        self.clicking(self.LOGIN_BTN)


    def error_message(self):
        error = self.get_text(self.ERROR_MSG)
        return error