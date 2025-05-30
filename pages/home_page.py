from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.loggers import setup_logger
from utils.constants import BASE_URL, VALID_USERNAME, VALID_PASSWORD

logger = setup_logger(__name__)

class HomePage(BasePage):
    HEADER_DIV = (By.ID, "login_button_container")
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def load(self):
        logger.info("Navegando a la homepage de saucedemo")
        self.open(BASE_URL)

    def wait_for_login_form(self):
        logger.info("Esperando por la login form")
        try:
            self.wait_for_element_visible(self.HEADER_DIV)
            logger.info("El login form se encontro correctamente")
            return True
        except Exception as e:
            logger.error(f"No se encontró el el login form: {e}")
            self.driver.save_screenshot("logs/header_not_found.png")
            raise
    
    def login(self, username=VALID_USERNAME, password=VALID_PASSWORD):
        logger.info(f"Try to log in with the given username and password: {username}, {password}")
        self.wait_for_element_visible(self.USERNAME).send_keys(username)
        self.wait_for_element_visible(self.PASSWORD).send_keys(password)
        self.wait_for_element_visible(self.LOGIN_BUTTON).click()
