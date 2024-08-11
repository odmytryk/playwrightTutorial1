from playwright.sync_api import Playwright, sync_playwright, expect
from test_ua_laout.links_in_menu import HomePageLinks

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    links_from_menu = HomePageLinks(page)

    links_from_menu.home_page_link.click()
    expect(page.locator("#comp-kqx72yrn1")).to_be_visible()

    links_from_menu.shop_women_link.click()
    expect(page.get_by_role("link", name="Shoes Price $")).to_be_visible()

    links_from_menu.shop_women_winter_link.click()
    expect(page.get_by_role("button", name="Load More")).to_be_visible()

    links_from_menu.look_book.click()
    expect(page.locator("#comp-kqx719jt2")).to_be_visible()

    links_from_menu.asked_questions.click()
    expect(page.get_by_text("Help Center")).to_be_visible()

    links_from_menu.contact_us.click()
    expect(page.get_by_placeholder("Enter your name")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
