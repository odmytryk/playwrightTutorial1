import playwright
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Playwright

#@pytest.fixture(scope="session")
@pytest.fixture(scope="function")
def set_up(page):
    #browser = playwright.chromium.launch(headless=False,slowMo=1000)
    #context = browser.new_context()
    #page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    yield page
@pytest.fixture
def setup_log_in(page):
    #browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    #context = browser.new_context()
    #page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

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
    page.get_by_label("Password").fill("test123")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    print("After steps")

    yield page
    page.close()