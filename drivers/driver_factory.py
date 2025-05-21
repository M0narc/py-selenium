import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_driver(browser_name="chrome"):
    is_ci = os.getenv("CI") == "true"

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if is_ci:
            options.add_argument("--headless=new")  # Para Chrome >= 109
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if is_ci:
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
