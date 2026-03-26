import pytest
from playwright.sync_api import Page,expect
from pages.home_page  import HomePage
from pages.bus_selection_page  import B
from conftest import  load_test_data 

test_data = load_test_data()
@pytest.mark.parametrize("data", test_data,ids=[d["test_case_id"] for d in test_data])

def test_101_booking(page:Page, data):
    home = HomePage(page)
    home.travel_details(data)
    home.search_by_details()
    


