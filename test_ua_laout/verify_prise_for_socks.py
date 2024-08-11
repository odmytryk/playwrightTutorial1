import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.get_by_role("link", name="Home").click()
    #page.pause()
    page.get_by_role("link", name="Shop Women", exact=True).click()

    all_links = page.get_by_role("link").all()
    for link in all_links:
        #print(link.text_content())
        if "$85.00" in link.text_content():
            print("test if")
            assert 'Schoes' not in link.text_content()
            #print(link.text_content(), link)

    expect(page.get_by_role("link", name="Shop Women", exact=True)).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
