import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://google.com")

    yield driver
    driver.quit()

def test_open_google(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title