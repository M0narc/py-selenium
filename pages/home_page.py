from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.loggers import setup_logger
from utils.constants import BASE_URL, VALID_USERNAME, VALID_PASSWORD, LOGIN_ER_MSJ
from utils.selectors import by_data_test

logger = setup_logger(__name__)

class HomePage(BasePage):
    HEADER_DIV = (By.ID, "login_button_container")
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ER_LOCATOR = by_data_test("error")

    def load(self):
        logger.info("Navegando a la homepage de saucedemo")
        self.open(BASE_URL)

    def wait_for_login_form(self):
        logger.info("Waiting for login form")
        try:
            self.wait_for_element_visible(self.HEADER_DIV)
            logger.info("Login form has been found")
            return True
        except Exception as e:
            logger.error(f"Login form could not be found: {e}")
            self.driver.save_screenshot("logs/header_not_found.png")
            raise
    
    def login(self, username=VALID_USERNAME, password=VALID_PASSWORD):
        logger.info(f"Try to log in with the given username and password: {username}, {password}")
        self.wait_for_element_visible(self.USERNAME).send_keys(username)
        self.wait_for_element_visible(self.PASSWORD).send_keys(password)
        self.wait_for_element_visible(self.LOGIN_BUTTON).click()

    def check_for_login_error_msg(self):
        return self.get_error_message(self.ER_LOCATOR , LOGIN_ER_MSJ)