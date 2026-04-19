from pages.login_page import LoginPage

def test_valid_login(driver):
    page = LoginPage(driver)

    page.open()
    page.login("tomsmith", "SuperSecretPassword!")

    message = page.get_message()
    assert "You logged into a secure area!" in message