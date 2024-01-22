from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class ProductsPage(BasePage):

    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    FIRST_ITEM = (By.ID, "item_4_title_link")

    def __init__(self, driver):
        super().__init__(driver)


    def check_products_displayed(self):
        return self.return_elements_amount(self.PRODUCT_ITEMS)


    def check_products_data(self):
        products = self.return_elements(self.PRODUCT_ITEMS)
        for item in products:
            print(item)


    def enter_product_page(self):
        self.clicking(self.FIRST_ITEM)
