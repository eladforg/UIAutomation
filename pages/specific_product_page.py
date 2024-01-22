from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class SpecificProductPage(BasePage):

    BACK_BTN = (By.ID, "back-to-products")


    def __init__(self, driver):
        super().__init__(driver)


    def click_back(self):
        self.clicking(self.BACK_BTN)