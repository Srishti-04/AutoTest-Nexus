import pytest
import json
from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger()

# Load test data
with open("testdata.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("username,password", [
    (d["username"], d["password"]) for d in test_data
])

def test_login(driver, username, password):
    # Step 1: Open login page
    # Step 2: Enter credentials
    # Step 3: Click login
    # Expected: Successful or failed login based on input

    logger.info(f"Testing login with username: {username}")

    page = LoginPage(driver)
    page.open()
    page.login(username, password)

    message = page.get_message().lower()

    if username == "tomsmith" and password == "SuperSecretPassword!":
        assert "secure area" in message, "Valid login failed"
    else:
        assert "invalid" in message, "Invalid login test failed"