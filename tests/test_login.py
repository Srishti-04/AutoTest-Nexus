import pytest
import json
from pages.login_page import LoginPage
from utils.logger import get_logger
logger = get_logger()

with open("testdata.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("username,password", [
    (d["username"], d["password"]) for d in test_data
])
def test_login(driver, username, password):
    logger.info("Starting login test")

    page = LoginPage(driver)
    page.open()
    page.login(username, password)

    message = page.get_message()

    if username == "tomsmith":
        assert "secure area" in message.lower()
    else:
        assert "invalid" in message.lower()