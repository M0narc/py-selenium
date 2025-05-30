import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("home_page")
class TestHomePage:
    def test_successful_login(self, home_page):
        assert home_page.get_title() == "Swag Labs", f"Expected title 'Swag Labs' but got '{home_page.get_title()}'"
        assert home_page.wait_for_login_form()
        home_page.login()
        assert "inventory" in home_page.get_url(), f"Expected 'inventory' in URL, but got {home_page.get_url()}"

    def test_unsuccessful_login(self, home_page):
        