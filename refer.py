
import re
import pytest
from playwright.sync_api import Page,expect

def test_example(page: Page) -> None:
    page.goto("https://www.abhibus.com/")
    page.get_by_role("textbox", name="Leaving From").click()
    page.get_by_role("textbox", name="Leaving From").fill("hyderabad")
    page.get_by_text("Hyderabad (All boarding").click()
    page.get_by_role("textbox", name="Going To").click()
    page.get_by_role("textbox", name="Going To").fill("tirupati")
    page.get_by_text("Tirupati (All drop points)").dblclick()
    page.locator(".container.text-input.input-wrapper.light.text > .container > div:nth-child(2)").click()
    page.locator("i > svg").click()
    page.get_by_role("button", name="24").click()
    page.get_by_role("button", name="Search").click()
    expect(page.get_by_text("BusesFlightsTrainsHotelsOffersTrack TicketNeed Help?Login/SignUp")).to_be_visible()
    page.locator("#group-service-TGSRTC a").filter(has_text="View Buses").click()
    page.locator("#show-service-btn-3856636178").click()
    page.locator("div").filter(has_text=re.compile(r"^Mgbs$")).first.click()
    page.locator("div").filter(has_text=re.compile(r"^Tirupati Bs$")).first.click()
    page.get_by_role("button", name="₹").first.click()
    page.get_by_role("button", name="Proceed").click()
    page.get_by_text("Skip").click()
    page.get_by_text("Trip DetailsHyderabad24 Apr").click()
    page.get_by_role("textbox", name="Mobile Number").click()
    page.get_by_role("textbox", name="Mobile Number").fill("90")
    page.get_by_role("textbox", name="Email ID").click()
    page.get_by_role("textbox", name="Email ID").fill("fgff")
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("ff")
    page.locator("#passenger-detail-age > .container.input-wrapper > .container.form-control").click()
    page.get_by_role("textbox", name="Age").fill("33")
    page.get_by_role("button", name="Male", exact=True).click()
    
def test_example2(page: Page) -> None:
    page.goto("https://www.abhibus.com/")
    page.get_by_role("textbox", name="Leaving From").click()
    page.get_by_role("textbox", name="Leaving From").fill("hyderabad")
    page.get_by_text("(All boarding points)").click()
    expect(page.get_by_role("textbox", name="Leaving From")).to_have_value("Hyderabad");
    page.get_by_role("textbox", name="Going To").click()
    page.get_by_role("textbox", name="Going To").fill("tirupati")
    page.locator("#aci-option-0").get_by_text("Tirupati").click()
    expect(page.get_by_role("textbox", name="Going To")).to_have_value("Tirupati");
    page.get_by_role("textbox", name="Onward Journey Date").click()
    page.locator("i > svg").click()
    page.get_by_role("button", name="3", exact=True).click()
    expect(page.get_by_role("textbox", name="Onward Journey Date")).to_have_value("03/04/2026");
    page.get_by_role("button", name="Search").click()
    page.locator("#group-service-TGSRTC a").filter(has_text="View Buses").click()
    page.locator("#show-service-btn-3776034357").click()
    page.locator("div").filter(has_text=re.compile(r"^Mgbs$")).first.click()
    page.get_by_text("Tirupati Bs04:0004 Apr").click()
    page.get_by_role("button", name="₹").first.click()
    page.get_by_role("button", name="₹").first.dblclick()
    page.get_by_role("button", name="Proceed").click()
    page.get_by_text("Skip").click()
