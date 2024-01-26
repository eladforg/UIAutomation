from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class CartPage(BasePage):

    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    CHECKOUT_BTN = (By.ID, "checkout")
    TEXT_YOUR_CART = (By.CSS_SELECTOR, ".title")
    TEXT_QTY = (By.CSS_SELECTOR, ".cart_quantity_label")
    TEXT_DESCRIPTION = (By.CSS_SELECTOR, ".cart_desc_label")
    LIST_PRODUCT_ITEMS = (By.CSS_SELECTOR, ".cart_item_label")
    LIST_REMOVE_BTNS = (By.CSS_SELECTOR, ".cart_button")
    ITEM_NUM = (By.CSS_SELECTOR, ".cart_quantity")

    def __init__(self, driver):
        super().__init__(driver)


    def check_default_elements_displayed(self):
        self.find_element(self.CONTINUE_SHOPPING_BTN)
        self.find_element(self.CHECKOUT_BTN)
        self.find_element(self.TEXT_YOUR_CART)
        self.find_element(self.TEXT_QTY)
        self.find_element(self.TEXT_DESCRIPTION)


    def click_continue_shopping_button(self):
        self.clicking(self.CONTINUE_SHOPPING_BTN)

    def click_checkout(self):
        self.clicking(self.CHECKOUT_BTN)

    def get_list_of_products(self):
        return self.return_elements(self.LIST_PRODUCT_ITEMS)

    def get_specific_product(self, product_num):
        products = self.get_list_of_products()
        return products[product_num]

    def get_product_description(self, product_num):
        return self.get_specific_product(product_num).text

    def remove_product(self, btn_num):
        remove_buttons = self.return_elements(self.LIST_REMOVE_BTNS)
        remove_buttons[btn_num].click()