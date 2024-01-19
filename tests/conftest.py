import os

import pytest
from _pytest.config import Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

import allure
from allure_commons.types import AttachmentType
from requests import Response


# for setting a global driver to be created before any run of class:
@pytest.fixture(scope='class', autouse=True)
def driver_init(request):
    global driver
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    driver.get("http://www.mytinytodo.net/demo/")
    driver.maximize_window()
    yield
    driver.quit()


# to create allure results report after every run:
def pytest_configure(config: Config) -> None:
    config.option.allure_report_dir = "allure-results"


# for global env. run:
def pytest_sessionFinish() -> None:
    environment_properties = {
     'browser': driver.name,
     'driver_version': driver.capabilities['browserVersion']
    }
    allure_env_path = os.path.join("allure-results", 'environment.properties')
    with open(allure_env_path, 'w') as f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        f.write(data)


# screenshot for failing test:
def pytest_exception_interact(report):
    if report.failed:
        allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)