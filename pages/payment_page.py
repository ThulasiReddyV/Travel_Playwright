from playwright.sync_api import Page,expect,TimeoutError
from pages.base_page  import BasePage
from pages.home_page import HomePage
from pages.passenger_page import PassengerPage
from utilities import timestamp
import re

class PaymentPage(PassengerPage):
    
    def __init__(self,page: Page):
        self.page = page
        self.details = page.locator(".mt-20.overflow-hidden.rounded-20.bg-common-white.pb-20.shadow-100")
        self.drop_expand = self.details.locator(".transition-transform.duration-150.justify-end")
        self.generate_qr = page.get_by_role("button", name="Generate QR")
        self.image = page.locator(".relative.rounded-10.p-10.shadow-100")
        self.image_class = page.locator(".transition-all.duration-500")
    
    def gen_qr(self):
        self.generate_qr.wait_for(state="visible")
        print(f"{self.generate_qr.text_content()}")
        self.generate_qr.click()     
        self.page.wait_for_load_state("networkidle")   
        self.image.wait_for(state="visible")
