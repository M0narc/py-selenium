import pytest
from drivers.driver_factory import get_driver

def pytest_addoption(parser):
    parser.addoption("--browser", 
                     action="store", 
                     default="chrome",
                     help="Browser to use: chrome or firefox")

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    driver = get_driver(browser_name)
    driver.maximize_window()
    yield driver
    driver.quit()
