import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

import utils.secret_config


#from home_page_elements import TestHomePage
@pytest.mark.parametrize("email, password", [("olha1@fake.com", "test123"),
                                             pytest.param("olha1@fake.com", "test123test123", marks=pytest.mark.xfail),
                                             pytest.param("nonono@fake.com", "test123", marks=pytest.mark.xfail)])
def test_tets_trarara(set_up, email, password) -> None:
    page = set_up

    print("Before test")
    page.wait_for_timeout(2000)
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


@pytest.mark.parametrize("email", ["olha1@fake.com",
                                             pytest.param("olha1@fake.com", marks=pytest.mark.xfail),
                                             pytest.param("nonono@fake.com", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", [ "test123",
                                             pytest.param("test123test123", marks=pytest.mark.xfail),
                                             pytest.param("test123", marks=pytest.mark.xfail)])
def test_tets_trarara_1(set_up, email, password) -> None:
    page = set_up

    print("Before test")
    page.wait_for_timeout(2000)
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


def test_tets_trarara_2(set_up) -> None:
    page = set_up

    print("Before test")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Log In").click()
    print("clicked login icon")
    page.get_by_test_id("signUp.switchToSignUp").click()
    print("clicked log in button")
    page.get_by_role("button", name="Log in with Email").click()
    print("clicked Log in with Email")
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("olha1@fake.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(utils.secret_config.PASSWORT)
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