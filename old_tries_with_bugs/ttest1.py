from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("about:blank")
    page.pause()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_label("Shoes gallery").get_by_text("Quick View").click()
    page.frame_locator("iframe[name=\"tpaModal_rtby_comp-kqx6zt2y2\"]").get_by_role("img", name="Shoes").click()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.get_by_role("button", name="Log In").click()
    print("Done")
    page.wait_for_timeout(20)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)