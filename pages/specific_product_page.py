from selenium.webdriver.common.by import By

from pages.basePage import BasePage
from pages.products_page import ProductsPage


# inherits from ProductsPage class so we can use its' cart actions (and anyway it includes BasePage class)
class SpecificProductPage(ProductsPage):

    BACK_BTN = (By.ID, "back-to-products")
    # CART_BTN = (By.CSS_SELECTOR, "a.shopping_cart_link")
    # CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    ITEM_DESC = (By.CSS_SELECTOR, ".inventory_details_desc_container")
    # ITEM_TITLE = (By.CSS_SELECTOR, ".inventory_details_name.large_size")
    # ITEM_CONTENT = (By.CSS_SELECTOR, ".inventory_details_desc.large_size")
    # ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_details_price")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "div.inventory_details_desc_container>button")


    def __init__(self, driver):
        super().__init__(driver)


    def click_back(self):
        self.clicking(self.BACK_BTN)


    def get_product(self):
        return self.find_element(self.ITEM_DESC)

    def get_item_description(self):
        return self.get_text(self.ITEM_DESC)


    def click_add_remove_to_cart_btn(self):
        self.clicking(self.ADD_TO_CART_BTN)

    # def get_item_title(self):
    #     return self.get_text(self.ITEM_TITLE)
    #
    #
    # def get_item_content(self):
    #     return self.get_text(self.ITEM_CONTENT)
    #
    #
    # def get_item_price(self):
    #     return self.get_text(self.ITEM_PRICE)



