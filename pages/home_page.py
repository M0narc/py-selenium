from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.loggers import setup_logger

logger = setup_logger(__name__)

class HomePage(BasePage):
    HEADER_DIV = (By.CLASS_NAME, "Header-module--header--aa06a")

    def load(self):
        logger.info("Navegando a la homepage")
        self.open("https://ecommercepractice.letskodeit.com/")

    def wait_for_header(self):
        logger.info("Esperando a que el encabezado esté visible")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.HEADER_DIV)
            )
            logger.info("El encabezado se encontró correctamente.")
            return True
        except Exception as e:
            logger.error(f"No se encontró el encabezado: {e}")
            self.driver.save_screenshot("logs/header_not_found.png")
            raise
