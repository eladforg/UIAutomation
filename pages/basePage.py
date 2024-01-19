import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select

class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver


    def fill_text(self, locator, text: str) -> None:
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def clicking(self, locator) -> None:
        self.driver.find_element(*locator).click()

    def convert_to_select_object(self, locator, sel_val) -> None:
        el=self.driver.find_element(*locator)
        dropdown = Select(el)
        dropdown.select_by_value(sel_val)

    def convert_to_select_object_by_index(self, locator, sel_indx) -> None:
        el=self.driver.find_element(*locator)
        dropdown = Select(el)
        dropdown.select_by_index(sel_indx)


    def return_elements(self, locator) -> int:
        results=self.driver.find_elements(*locator)
        print(f"There are {len(results)} results")
        return len(results)
