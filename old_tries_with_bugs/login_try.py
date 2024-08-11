from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("button", name="Sign up with email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symonstori")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("ArrowLeft")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("ArrowLeft")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("ArrowLeft")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("ArrowLeft")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("ArrowLeft")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("ArrowLeft")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("ArrowRight")
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.stori")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("ArrowRight")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("ArrowRight")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("ArrowRight")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("ArrowRight")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("ArrowRight")
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("test123")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").dblclick()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").press("ArrowLeft")
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("Olha.Dmytryk@gmail.com")
    page.frame_locator("iframe[name=\"a-k61ogmslqy94\"]").locator(".rc-anchor-center-item").first.click()
    with page.expect_popup() as page1_info:
        page.get_by_text("New to this site?Sign UpLog").click()
    page1 = page1_info.value
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("submit").get_by_test_id("buttonElement").dblclick()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
