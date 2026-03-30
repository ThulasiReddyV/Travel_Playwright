from playwright.sync_api import Page,expect,TimeoutError
from pages.base_page  import BasePage
from pages.home_page import HomePage
import re

class BusPage(HomePage):

    def __init__(self,page: Page):
        self.page = page
        
        self.available_buses = page.locator(".buses-availability")
        self.service_pro_group_card = page.locator("#group-service-TGSRTC")
        self.bp_dp_container = page.locator(".row.seating-place-selector")
        self.all_seats = page.locator(".Tooltip-Wrapper")

        self.radio_container =  ".container.radio-container.light.neutral.lg"
        self.dark_pop_up_loc = ".Tooltip-Tip.bottom.dark"
        self.proceed = page.get_by_role("button", name="Proceed")
        self.skip = page.get_by_text("Skip")
        self.no_servie_msg = page.get_by_role("heading", level=5)
        
        

    def avb_buses_count(self):
        msg = ""
        buses_count = []
        try:
            msg = self.available_buses.text_content()
            print(msg)
            buses_count = re.findall(r'\d+', msg)
            
                
        except TimeoutError:
            pass
        return len(buses_count)  ,msg   


           
    def no_service_msg_fun(self):
        no_ser_msg=""
        try:
            no_ser_msg = self.no_servie_msg.text_content()
            print(no_ser_msg)
            return no_ser_msg

        except TimeoutError:
            pass
    
    
    def view_service_provider(self):
        self.page.wait_for_timeout(3000)

        service_provider_buses_info = self.service_pro_group_card.locator(".text-truncate").all()

        for ele in service_provider_buses_info:
            print(f"{ele.text_content()}")


        self.view_buses = self.service_pro_group_card.filter(has_text="View Buses")
        self.view_buses.wait_for(state="visible",timeout=1000)

        self.view_buses.click()
        #self.page.wait_for_timeout(5000)

    def find_bus(self,service_no):
   
        self.whole_bus_container = self.service_pro_group_card.locator(".container.card.service.light.rounded-md").filter(has_text=service_no)
        if self.whole_bus_container.count() == 0:
            print(f"No bus Container with {service_no}")
            return 
        
        self.select_seat = self.whole_bus_container.locator("button[id*='service']").filter(has_text="Select Seats")
        self.select_seat.wait_for(state="visible",timeout=10000)

        self.select_seat.click()
        no_bss  = self.whole_bus_container.filter(has_text="Hide Seats")
        if no_bss.count() == 1:
            print(f"{service_no} Bus found ")
            return False

        else:
            print(f"{service_no} Bus not found ")
            return True

    def select_bp_dp(self,data):
        self.page.wait_for_timeout(5000)

        if self.bp_dp_container.count() >1:
            print("Many Boarding Points and Dropping Points opened")
            return
        
        self.bp_text = self.bp_dp_container.locator(self.radio_container).filter(has_text=data["boarding_pt"].capitalize())
        self.bp_text.wait_for(state="visible", timeout=1000)
        print(f"{self.bp_text.text_content()}")
        self.bp_text.click(force=True)


        self.dp_text = self.bp_dp_container.locator(self.radio_container).filter(has_text=data["dropping_pt"].capitalize())
        self.dp_text.wait_for(state="visible", timeout=1000)
        print(f"{self.dp_text.text_content()}")
        self.dp_text.click(force=True)
        

    def find_seat(self,seat_no):

        #.page.wait_for_timeout(5000)  
        self.all_seats.first.wait_for(state="visible", timeout=10000)

        all_seats_ele = self.all_seats.all()
        print(f"Total seats: {len(all_seats_ele)}")

        for seat in all_seats_ele:
            
            seat.hover()
            self.page.wait_for_timeout(300)  
            seat.scroll_into_view_if_needed()
     
            try:
                self.dark_pop_up = seat.locator(self.dark_pop_up_loc)
            
                desired_seat = self.dark_pop_up.locator("span").filter(has_text=re.compile(rf"^{seat_no}$"))  
                desired_seat.wait_for(state="visible", timeout=250)
                desired_seat.scroll_into_view_if_needed()
                print(f"{desired_seat.text_content()} is selected")
                seat.click()

                return True
            except TimeoutError:
                continue
                    
        print(f"Seat {seat_no} already booked or not found")
        return False


    def proceed_to_enter_details(self):
        self.proceed.click()
        self.skip.wait_for(state="visible", timeout=1000)
        self.skip.click()

        




