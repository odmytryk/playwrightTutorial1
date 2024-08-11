import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
#from home_page_elements import TestHomePage
@pytest.mark.parametrize("email, password", [("olha1@fake.com", "test123"),
                                             pytest.param("olha1@fake.com", "test123test123", marks=pytest.mark.xfail),
                                             pytest.param("nonono@fake.com", "test123", marks=pytest.mark.xfail)])
def test_tets_trarara(set_up, email, password) -> None:
    page = set_up

    print("Before test")

    page.get_by_role("button", name="Log In").click()
    print("clicked login icon")
    page.get_by_test_id("signUp.switchToSignUp").click()
    print("clicked log in button")
    page.get_by_role("button", name="Log in with Email").click()
    print("clicked Log in with Email")
    page.get_by_test_id("emailAuth").get_by_label("Email").fill(email)
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(password)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    print("After steps")
    #page.pause()

    # home_page = TestHomePage(page)
    # expect(home_page.celebrate_header).to_contain_text("Celebrating")
    # expect(home_page.celebrate_body).to_be_visible()
    expect(page.get_by_label("olha1 account menu")).to_be_visible()
    print("After test")

    # ---------------------



# with sync_playwright() as playwright:
#     run(playwright)