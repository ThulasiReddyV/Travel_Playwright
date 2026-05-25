import re
import pytest
from playwright.sync_api import Page,expect

def test_train(page : Page):
    page.goto("https://www.abhibus.com/")
    expect(page).to_have_title(re.compile(r".*Book Bus.*"))
    page.set_viewport_size({"width": 1920, "height": 1080})
    #from_city = page.get_by_placeholder("Leaving From").click()
    from_city = page.get_by_placeholder("Leaving From")
    from_city.fill("hyderabad")
    sel = page.locator("xpath=//li[@id='aci-option-0']//span[normalize-space()]")
    sel.click()
    page.wait_for_timeout(5000)







