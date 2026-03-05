from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    # Selenium Manager cuida do driver automaticamente
    driver = webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    msg = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in msg

    driver.quit()