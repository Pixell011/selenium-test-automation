from pages.login_page import LoginPage


def test_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")

    assert "erro proposital" in page.get_message()
