from playwright.sync_api import Page,expect,TimeoutError
from pages.home_page import HomePage


class BusPage(HomePage):

    def __init__(self,page: Page):
        self.page = page
        
        self.available_buses = page.locator(".buses-availability")
        self.service_pro_group_card = page.locator("#group-service-TGSRTC")
        

    def avb(self):
        
        print(self.available_buses.text_content())

    def view_service_provider(self):
        self.page.wait_for_timeout(3000)

        #self.service_pro_group_card.scroll_into_view_if_needed()
        service_provider_buses_info = self.service_pro_group_card.locator(".text-truncate").all()

        for ele in service_provider_buses_info:
            print(f"{ele.text_content()}")


        self.view_buses = self.service_pro_group_card.filter(has_text="View Buses")
        self.view_buses.wait_for(state="visible",timeout=1000)

        self.view_buses.click()
        #self.page.wait_for_timeout(5000)

    def find_bus(self,service_no):
   
        self.whole_bus_conatiner = self.service_pro_group_card.locator(".row.card-body.service-info").filter(has_text=service_no)
        if self.whole_bus_conatiner.count() == 0:
            print(f"No bus with {service_no}")
            return
        
        """self.bus_info = whole_bus_conatiner.first
        self.bus_info.wait_for(state="visible",timeout=10000)
        self.bus_info.scroll_into_view_if_needed()
        self.page.wait_for_timeout(5000)"""
        
        #self.parent = self.whole_bus_conatiner.locator(".row.card-body.service-info")

        self.select_seat = self.whole_bus_conatiner.locator("button[id*='service']").filter(has_text="Select Seats")
        self.select_seat.wait_for(state="visible",timeout=10000)
        #print(f"{self.select_seat.text_content()}")

        self.select_seat.click()
        no_bss  = self.whole_bus_conatiner.filter(has_text="Hide Seats")
        if no_bss.count() == 1:
            print(f" {service_no} Seats expanded ")
        else:
            print(f" {service_no} Seats not found ")
        self.page.wait_for_timeout(5000)

    def find_seat(self,seat_no):


        pass




