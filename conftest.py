from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--ignore-certificate-errors")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)   # fallback wait

    yield driver
    driver.quit()