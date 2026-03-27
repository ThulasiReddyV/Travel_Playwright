from playwright.sync_api import Page,expect,TimeoutError
from pages.home_page import HomePage
import re

class PassengerPage(HomePage):

    def __init__(self,page: Page):
        self.page = page
        self.mobile_num =page.get_by_role("textbox", name="Mobile Number")
        self.email =page.get_by_role("textbox", name="Email ID")
        self.name =page.get_by_role("textbox", name="Name")
        self.age =page.get_by_role("textbox", name="Age")
        self.continue_to_Pay_btn = page.get_by_text(re.compile(r"^Continue to Pay"))



    def passenger_details(self,data):
        
        self.enter_passenger_name(data["pass_name"])
        self.enter_passenger_age(data["pass_age"])
        self.enter_passenger_mobile_num(data["pass_mobile"])
        self.enter_passenger_email(data["pass_email"])
        self.enter_passenger_gender(data["pass_gender"])


       

    def enter_passenger_name(self,detail):
        passenger_name = self.name
        passenger_name.wait_for(state="visible", timeout=1000)

        passenger_name.click()
        passenger_name.fill(detail)
        print(f"Name:{passenger_name.get_attribute('value')}")

    def enter_passenger_age(self,detail):
        passenger_age = self.age
        passenger_age.wait_for(state="visible", timeout=1000)

        passenger_age.click()
        passenger_age.fill(detail)
        print(f"Age:{passenger_age.get_attribute('value')}")


    def enter_passenger_gender(self,detail):
        passenger_gender = self.page.get_by_role("button", name=f"{detail}", exact=True)
        passenger_gender.wait_for(state="visible", timeout=1000)

        passenger_gender.click()
        #check_gender_li = f".btn.btn-gender.{detail}.inactive.light.outlined.neutral.sm.rounded-md.inactive.button"
        check_gender = self.page.locator(f".btn.btn-gender.{detail}.inactive.light.outlined.neutral.sm.rounded-md.inactive.button")
        if check_gender.count == 1:
            print(f"{detail} is selected")



    def enter_passenger_mobile_num(self,detail):
        passenger_mobile = self.mobile_num
        passenger_mobile.wait_for(state="visible", timeout=1000)
        passenger_mobile.click()
        passenger_mobile.fill(detail)
        print(f"Mobile Number:{passenger_mobile.get_attribute('value')}")


    def enter_passenger_email(self,detail):
        passenger_email = self.email
        passenger_email.wait_for(state="visible", timeout=1000)
        passenger_email.click()
        passenger_email.fill(detail)
        print(f"Email:{passenger_email.get_attribute('value')}")

    def continue_to_Pay(self):
        self.continue_to_Pay_btn.click()
        self.page.wait_for_timeout(10000)



