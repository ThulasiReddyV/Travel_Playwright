import pytest
from playwright.sync_api import Page,expect
from pages.base_page  import BasePage
from pages.home_page  import HomePage
from pages.bus_selection_page  import BusPage

from conftest import  load_test_data
from utilities import timestamp

import re


test_data = load_test_data()
@pytest.mark.parametrize("data", test_data,ids=[d["test_case_id"] for d in test_data])

def test_102_bus_and_seat_page(page:Page, data):
    base = BasePage(page)
    id = data["test_case_id"]

    home = HomePage(page)
    expect(page).to_have_url(re.compile(r".*abhibus.*",re.IGNORECASE))

    if not home.to_proceed(home.travel_details(data),id):
        return
    home.search_by_details()
    expect(page).to_have_url(re.compile(rf".*{re.escape(data['from_loc'])}.*{re.escape(data['to_loc'])}.*{re.escape(data['date_of_journey'].replace('/','-'))}.*",re.IGNORECASE))

    bus = BusPage(page)
    available, msg = bus.avb_buses_count()
    if not available and msg =="":
        print(bus.no_servie_msg.text_content())
        page.screenshot(path=f"screenshots/{data['test_case_id']}_{timestamp()}.png")
        expect(bus.no_servie_msg).to_contain_text("There are no services")
        return

    bus.view_service_provider()
    if not bus.to_proceed(bus.find_bus(data["bus_ser_no"]),id):
        return

    bus.select_bp_dp(data)
    if not bus.to_proceed(bus.find_seat(data["seat_no"]),id):
        return
    
    bus.proceed_to_enter_details()
    expect(page).to_have_url(re.compile(r".*passengerinfo.*",re.IGNORECASE))


