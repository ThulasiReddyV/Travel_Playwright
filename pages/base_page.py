from playwright.sync_api import Page,expect
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from conftest import *
from utilities import *

from datetime import datetime,timedelta


class BasePage:

    def __init__(self,page: Page):
        self.page = page

        self.error = page.locator(".error")
        self.pass_error = page.locator(".container.single-error-msg")

    def to_proceed(self,info,test_case_id):
        if not info :
            self.page.screenshot(path=f"screenshots/{test_case_id}_{timestamp()}.png")
            return False
        return True
        
   