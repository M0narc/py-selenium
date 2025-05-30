from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.loggers import setup_logger

logger = setup_logger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        logger.info(f"Open URL: {url}")
        self.driver.get(url)

    def get_title(self):
        title = self.driver.title
        logger.info(f"Page title: {title}")
        return title
    
    def get_url(self):
        current_url = self.driver.current_url
        logger.info(f"Current URL: {current_url}")
        return current_url

    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
            )