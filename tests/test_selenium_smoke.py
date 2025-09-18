from selenium import webdriver
from selenium.webdriver.common.by import By


def test_example_domain():
    driver = webdriver.Chrome()  # Selenium Manager сам подтянет драйвер
    driver.get("https://example.com")
    h1 = driver.find_element(By.TAG_NAME, "h1").text
    assert "Example Domain" in h1
    driver.quit()
    print("Selenium OK")
