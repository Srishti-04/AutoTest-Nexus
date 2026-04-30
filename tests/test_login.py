from pages.login_page import LoginPage
def test_search(driver):
    page = LoginPage(driver)
    page.open()
    page.search("Selenium Testing")

    assert "Selenium" in driver.title