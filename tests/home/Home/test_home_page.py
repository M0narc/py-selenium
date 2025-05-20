from pages.home_page import HomePage

def test_home_page_title(browser):
    home_page = HomePage(browser)
    home_page.load()
    assert "Let's Kode It" in home_page.get_title()
