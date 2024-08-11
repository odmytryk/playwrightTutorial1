class HomePageLinks:
    def __init__(self, page):
        self.home_page_link = page.get_by_label("Site").get_by_role("link", name="Home")
        self.shop_women_link = page.get_by_role("link", name="Shop Women", exact=True)
        self.shop_women_winter_link = page.get_by_role("link", name="Shop Women Winter")
        self.look_book = page.get_by_role("link", name="Look Book")
        self.asked_questions = page.get_by_role("link", name="FAQ")
        self.contact_us = page.get_by_role("link", name="Contact Us")

