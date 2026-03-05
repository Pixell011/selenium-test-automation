from pages.login_page import LoginPage


def test_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in page.get_message()
