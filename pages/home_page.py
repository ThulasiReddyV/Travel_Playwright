from playwright.sync_api import Page,expect
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from conftest import *
from utilities import *
from pages.base_page import BasePage

from datetime import datetime,timedelta

class HomePage(BasePage):

    def __init__(self,page: Page):
        self.page = page

        self.from_city = page.get_by_role("textbox", name="Leaving From")
        self.to_city = page.get_by_role("textbox", name="Going To")
        self.suggestion =  page.locator("xpath=//li[@id='aci-option-0']//span[normalize-space()]")
        self.calender = page.get_by_placeholder("Onward Journey Date")
        self.next_month_btn = page.locator(".calender-month-change>i > svg")
        self.submit = page.get_by_role("button", name="Search")
        self.error = page.locator(".error")

   
    def enter_from(self,city):
        self.from_city.click()
        self.from_city.fill(city)
        self.suggestion.click()
        print(f"\nFrom: {self.from_city.get_attribute('value')}")

    def enter_to(self,city):   
        self.to_city.click()
        self.to_city.fill(city)
        self.suggestion.click()
        print(f"To: {self.to_city.get_attribute('value')}")


    def select_date_of_journey(self, date):
    
        selected_date = datetime.strptime(date,"%d/%m/%Y")
        today = datetime.today()
        if selected_date.date() < today.date():
            print("Past Date")
            return False
        elif selected_date.date() > today.date() + timedelta(days=90):
            print("3 months future Date")
            return False
        else:
            self.calender.click()

            day,month,year = dd_mm_yy_convert(date)
            dept_date = f'a[role="button"][data-date="{day}"][data-month="{month}"][data-year="{year}"]'
            #self.departure_date = self.page.locator(dept_date).click()
            self.in_month(dept_date)
            print(f"Date of Journey: {self.calender.get_attribute('value')}")
            return True

       
    
    def in_month(self, departure_date, attempts=0):
        if attempts >= 3:
            print("Could not find date after 3 months")
            return
        try:
            self.page.locator(departure_date).wait_for(state="visible", timeout=5000)
            self.page.locator(departure_date).click()
        except PlaywrightTimeoutError:
            self.next_month(departure_date, attempts)

    def next_month(self, departure_date, attempts):
        try:
            self.next_month_btn.last.wait_for(state="visible", timeout=3000)
            self.next_month_btn.last.click()
            self.in_month(departure_date, attempts + 1)
        except TimeoutError:
            self.lastmonth_loaded = True
            print("Loaded upto Last Month")


    

    def travel_details(self,data):
        self.enter_from(data["from_loc"])
        self.enter_to(data["to_loc"])
        proo= self.select_date_of_journey(data["date_of_journey"])
        return proo

        
    
    def search_by_details(self):
        self.submit.click()

      