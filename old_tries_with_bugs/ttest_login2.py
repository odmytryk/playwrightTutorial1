from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    print('Start')
    contact_us_form_ola = ContactUsPage(page)

    contact_us_form_ola.submit_form("Olha", "home", "ol@gm.co", "123123", "text test", "happy")
    # page.pause()
    page.get_by_role("button", name="Submit").click()
    time.sleep(6)
    expect(page.get_by_text("Thanks")).to_be_visible()
    print("after")
    #page.pause()
    expect(page.get_by_placeholder("Enter your name")).to_be_visible()
    print("Done")


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
