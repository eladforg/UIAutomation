import os

import pytest
from _pytest.config import Config
from _pytest.fixtures import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

import allure
from allure_commons.types import AttachmentType
from requests import Response

from pages.loginPage import LoginPage


# for setting a global driver to be created before any run of class:
@pytest.fixture(scope='class', autouse=True)
def driver_init(request):
    global driver
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield
    #driver.quit()


# to create allure results report after every run:
def pytest_configure(config: Config) -> None:
    config.option.allure_report_dir = "allure-results"



# screenshot for failing test:
def pytest_exception_interact(report):
    if report.failed:
        allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)


#
# @fixture
# def login():
#     p_login = LoginPage(driver)
#     p_login.login("standard_user", "secret_sauce")