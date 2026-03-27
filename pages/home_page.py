from playwright.sync_api import Page,expect
from conftest import dd_mm_yy_convert




class HomePage:

    def __init__(self,page: Page):
        self.page = page

        self.from_city = page.get_by_role("textbox", name="Leaving From")
        self.to_city = page.get_by_role("textbox", name="Going To")
        self.suggestion =  page.locator("xpath=//li[@id='aci-option-0']//span[normalize-space()]")
        self.calender = page.get_by_placeholder("Onward Journey Date")
        self.submit = page.get_by_role("button", name="Search")


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
        self.calender.click()
        day,month,year = dd_mm_yy_convert(date)
        dept_date = f'a[role="button"][data-date="{day}"][data-month="{month}"][data-year="{year}"]'
        self.departure_date = self.page.locator(dept_date).click()
        print(f"Date of Journey: {self.calender.get_attribute('value')}")



    def travel_details(self,data):
        self.enter_from(data["from_loc"])
        self.enter_to(data["to_loc"])
        self.select_date_of_journey(data["date_of_journey"])
    
    def search_by_details(self):
        self.submit.click()

      