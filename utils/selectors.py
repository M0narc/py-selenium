from selenium.webdriver.common.by import By

def by_data_test(value: str):
    """
    Returns a Selenium locator for elements with a specific data-test attribute.

    Example:
        by_data_test("error") => (By.CSS_SELECTOR, "[data-test='error']")
    """
    return (By.CSS_SELECTOR, f"[data-test='{value}']")