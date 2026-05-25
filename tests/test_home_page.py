import pytest
from playwright.sync_api import Page,expect
from pages.base_page  import BasePage
from pages.home_page  import HomePage
from conftest import  load_test_data 
import re

test_data = load_test_data()
@pytest.mark.parametrize("data", test_data,ids=[d["test_case_id"] for d in test_data])

def test_101_booking_page(page:Page, data):
    base = BasePage(page)
    id = data["test_case_id"]

    home = HomePage(page)
    expect(page).to_have_url(re.compile(r".*abhibus.*",re.IGNORECASE))

    if not home.to_proceed(home.travel_details(data),id):
        return
    home.search_by_details()
    expect(page).to_have_url(re.compile(rf".*{re.escape(data['from_loc'])}.*{re.escape(data['to_loc'])}.*{re.escape(data['date_of_journey'].replace('/','-'))}.*",re.IGNORECASE))



