import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

class TestSmoke:

    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless")  # Run in headless mode
        self.driver = webdriver.Firefox(options=options)
        self.driver.implicitly_wait(10)  # Wait up to 10 seconds for elements
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_home_page_title(self):
        self.driver.get("http://127.0.0.1:5500/index.html")  # or whatever your homepage file is
        assert "Home" in self.driver.title or "My Website" in self.driver.title

    def test_element_on_page(self):
        self.driver.get("http://127.0.0.1:5500/index.html")
        heading = self.driver.find_element(By.TAG_NAME, "h1")
        assert heading.is_displayed()
