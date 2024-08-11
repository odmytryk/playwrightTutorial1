import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.get_by_role("link", name="Shop Women", exact=True).click()
    product = page.get_by_text("$85.00").nth(0).get_by_text("Shoes")
    assert product != 'Socks'
    print(product)

    #expect(page.locator("xpath=//wow-image").nth(1)).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
