import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("button", name="Sign up with email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("Olha@fake.comm")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("Test1234")
    page.frame_locator("iframe[name=\"a-309a5uhvrzjg\"]").get_by_label("I'm not a robot").click()
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
