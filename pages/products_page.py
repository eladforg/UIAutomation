from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class ProductsPage(BasePage):

    LIST_PRODUCT_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    FIRST_ITEM = (By.ID, "item_4_title_link")
    LIST_ADD_TO_CART_BTNS = (By.CSS_SELECTOR, "button.btn")
    FILTER_BTN = (By.TAG_NAME, "select")
    CART_BTN = (By.CSS_SELECTOR, "a.shopping_cart_link")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    BURGER_BTN = (By.ID, "react-burger-menu-btn")
    MENU_ALL_ITEMS_BTN = (By.ID, "inventory_sidebar_link")
    MENU_ABOUT_BTN = (By.ID, "about_sidebar_link")
    MENU_LOGOUT_BTN = (By.ID, "logout_sidebar_link")
    MENU_RESET_BTN = (By.ID, "reset_sidebar_link")


    def __init__(self, driver):
        super().__init__(driver)


    def check_products_displayed(self):
        return self.return_elements_amount(self.LIST_PRODUCT_ITEMS)


    def products_list(self):
        products = self.return_elements(self.LIST_PRODUCT_ITEMS)
        return products


    def add_to_cart_btns_list(self):
        return self.return_elements(self.LIST_ADD_TO_CART_BTNS)


    def add_remove_item_to_cart(self, btn_number):
        buttons = self.add_to_cart_btns_list()
        print(f"button number {buttons[btn_number].text}")
        if 0 <= btn_number < len(buttons):
            buttons[btn_number].click()
        else:
            print(f"button number {btn_number} is out of bounds")


    def check_cart_badge(self):
        return self.get_text(self.CART_BADGE)


    def enter_product_page(self):
        self.clicking(self.FIRST_ITEM)
