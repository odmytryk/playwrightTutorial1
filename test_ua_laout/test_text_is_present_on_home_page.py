from playwright.sync_api import Playwright, sync_playwright, expect
from test_ua_laout.home_page_elements import TtestHomePage
import pytest

def test_celebrate_header_is_present(log_in) -> None:
    page = log_in
    home_page = TtestHomePage(page)
    expect(home_page.celebrate_header).to_contain_text("Celebrating")


@pytest.mark.skip(reason="not reeaadyy daddy")
def test_celebrate_body_is_present(set_up) -> None:
    page = set_up
    home_page = TtestHomePage(page)
    expect(home_page.celebrate_body).to_be_visible()
    expect(page.get_by_role("button", name="Shop Now")).to_be_visible()

#@pytest.mark.xfail(reason="development is still not ready")
def test_shop_now_button_is_present(setup_log_in) -> None:
    page = setup_log_in
    expect(page.get_by_role("button", name="Shop Now")).to_be_visible()

@pytest.mark.integration
@pytest.mark.smoke
def test_shop_now_button_is_present_2(setup_log_in) -> None:
    page = setup_log_in
    expect(page.get_by_role("button", name="Shop Now")).to_be_visible()


@pytest.mark.smoke
def test_shop_now_button_is_present_3(setup_log_in) -> None:
    page = setup_log_in
    expect(page.get_by_role("button", name="Shop Now")).to_be_visible()

def test_shop_now_button_is_present_4(setup_log_in) -> None:
    page = setup_log_in
    expect(page.get_by_role("button", name="Shop Now")).to_be_visible()


@pytest.mark.smoke
def test_shop_now_button_is_present_5(setup_log_in) -> None:
    page = setup_log_in
    expect(page.get_by_role("button", name="Shop Now")).to_be_visible()
