import os
import pytest
import allure
from drivers.driver_factory import get_driver

def pytest_addoption(parser):
    parser.addoption("--browser", 
                     action="store", 
                     default="chrome",
                     help="Browser to use: chrome or firefox")
    parser.addoption("--headless", 
                     action="store_true", 
                     help="Run browser in headless mode")

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless_flag = request.config.getoption("--headless")
    
    # Force headless if running in CI environment
    is_ci = os.getenv("CI", "").lower() == "true"
    headless = headless_flag or is_ci

    driver = get_driver(browser_name=browser_name, headless=headless)
    driver.maximize_window()
    yield driver

    # Screenshot in case of error
    if request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Hook to check if a test has failed.
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
