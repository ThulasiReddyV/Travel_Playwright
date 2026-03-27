import pytest
from playwright.sync_api import Page,expect
from pages.home_page  import HomePage
from pages.bus_selection_page  import BusPage
from pages.passenger_page import PassengerPage
from pages.payment_page import Paymentpage

from conftest import  load_test_data 
import re

test_data = load_test_data()
@pytest.mark.parametrize("data", test_data,ids=[d["test_case_id"] for d in test_data])

def test_103_booking(page:Page, data):
    home = HomePage(page)
    expect(page).to_have_url(re.compile(r".*abhibus.*"),re.IGNORECASE)

    home.travel_details(data)
    home.search_by_details()
    expect(page).to_have_url(re.compile(rf".*{re.escape(data['from_loc'])}.*{re.escape(data['to_loc'])}.*"),re.IGNORECASE)

    bus = BusPage(page)
    bus.avb()
    bus.view_service_provider()
    bus.find_bus(data["bus_ser_no"])
    bus.select_bp_dp(data)
    
    bus.find_seat(data["seat_no"])
    bus.proceed_to_enter_details()
    expect(page).to_have_url(re.compile(r".*passengerinfo.*"),re.IGNORECASE)
    
    passenger = PassengerPage(page)
    passenger.passenger_details(data)
    passenger.continue_to_Pay()
    expect(page).to_have_url(re.compile(r".*payments.*"),re.IGNORECASE)

    payment = Paymentpage(page)
    payment.gen_qr()



