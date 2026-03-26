#from selenium import webdriver
import pytest
from playwright.sync_api import Page

import json
import os
from utilities import *
from datetime import datetime



@pytest.fixture(scope="session")
def config_load():
    return read_json("config.json")
    

@pytest.fixture(scope="function")
def page(page : Page ,config_load):

    page.goto(config_load["base_url"])
    #page.set_viewport_size({"width": 1920, "height": 1080})
    #page.goto("https://www.abhibus.com/")
    #.goto("https://www.abhibus.com/", timeout=60000, wait_until="domcontentloaded")
    #driver.maximize_window()
    yield page
    #take_screenshot(driver,'Page_Upto_Processed')
    #page.close()

"""def driver(config_load):
    driver= webdriver.Chrome()
    driver.get(config_load["base_url"])
    driver.maximize_window()
    yield driver
    #take_screenshot(driver,'Page_Upto_Processed')
    driver.quit()"""

def pytest_configure(config):
    reports_dir = "reports"
    os.makedirs(reports_dir,exist_ok = True)
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    if config.args:
        test_name = os.path.splitext(os.path.basename(config.args[0]))[0]
        report_name = f"{test_name}_{timestamp}.html"
    else:
        report_name = f"report_{timestamp}.html"
    config.option.htmlpath = os.path.join(reports_dir,report_name)