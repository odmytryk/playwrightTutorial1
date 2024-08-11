from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://deutsch-online.com.ua/")
    with page.expect_popup() as page1_info:
        page.locator("div:nth-child(12) > div:nth-child(2) > div:nth-child(2) > .et_pb_button_module_wrapper > .et_pb_button").click()
    page1 = page1_info.value
    with page1.expect_popup() as page2_info:
        page1.get_by_role("link", name="Придбати 5").click()
    page2 = page2_info.value
    #page2.pause()
    page.wait_for_load_state("networkidle")
    #expect(page2.get_by_text("E-mail: info.liebentritt@")).to_be_visible()
    print("DONE")
    page2.get_by_role("link", name="Instagram").click()
    #expect(page2.get_by_text("Allow the use of cookies from")).to_contain_text()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
