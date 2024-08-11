import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.get_by_role("link", name="Shop Women", exact=True).click()
    page.get_by_role("link", name="Shoes Price $").click()
    print("Before test")
    page.locator("div:nth-child(2) > .s__8myoX6 > .s__8RwS1w > .syjsn7Y > .s__1KAKps > .sNpVAky").click()
    page.get_by_label("Quantity").click()
    page.locator("label span").nth(2).click()
    page.locator("label span").nth(1).click()
    page.get_by_label("Quantity").click()
    print("After test")
    page.pause()
    expect(page.get_by_role("heading", name="PRODUCT INFO")).to_be_visible()
    #expect(page.get_by_text("I'm a product description. I'")).to_be_hidden()
    print("alles")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
