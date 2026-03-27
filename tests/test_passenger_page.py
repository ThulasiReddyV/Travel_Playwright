import pytest
from playwright.sync_api import Page,expect
from pages.home_page  import HomePage
from pages.bus_selection_page  import BusPage
from pages.passenger_page import PassengerPage

from conftest import  load_test_data 

test_data = load_test_data()
@pytest.mark.parametrize("data", test_data,ids=[d["test_case_id"] for d in test_data])

def test_103_booking(page:Page, data):
    home = HomePage(page)
    home.travel_details(data)
    home.search_by_details()
    bus = BusPage(page)
    bus.avb()
    bus.view_service_provider()
    bus.find_bus(data["bus_ser_no"])
    bus.select_bp_dp(data)
    
    bus.find_seat(data["seat_no"])
    bus.proceed_to_enter_details()
    passenger = PassengerPage(page)
    passenger.passenger_details(data)
    passenger.continue_to_Pay()


