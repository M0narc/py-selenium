import pytest
from utils.constants import INVALID_USERNAME, LOGIN_ER_MSJ, PAGE_TITLE

@pytest.mark.usefixtures("home_page")
class TestHomePage:

    def test_successful_login(self, home_page):
        assert home_page.get_title() == f"{PAGE_TITLE}", f"Expected title '{PAGE_TITLE}' but got '{home_page.get_title()}'"
        assert home_page.wait_for_login_form()
        home_page.login()
        assert "inventory" in home_page.get_url(), f"Expected 'inventory' in URL, but got {home_page.get_url()}"

    def test_unsuccessful_login(self, home_page):
        home_page.login(INVALID_USERNAME, "asdasdsa")
        actual_msj = home_page.check_for_login_error_msg()
        assert actual_msj == LOGIN_ER_MSJ
