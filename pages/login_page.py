from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # XPath locator (important for resume/interview)
    search_box = (By.XPATH, "//textarea[@name='q']")

    def open(self):
        self.driver.get("https://www.google.com")

    def search(self, text):
        self.driver.find_element(*self.search_box).send_keys(text + Keys.RETURN)