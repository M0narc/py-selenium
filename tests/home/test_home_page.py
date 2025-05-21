from pages.home_page import HomePage

def test_homepage_header_visible(browser):
    home = HomePage(browser)
    home.load()
    assert home.wait_for_header()
