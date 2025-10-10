import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com")
driver.find_element(By.ID, "APjFqb").send_keys("India")
driver.find_element(By.NAME, "btnK").click()
time.sleep(5)
driver.quit()
