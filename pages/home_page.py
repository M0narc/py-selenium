from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://ecommercepractice.letskodeit.com/"

    def load(self):
        self.open(self.URL)