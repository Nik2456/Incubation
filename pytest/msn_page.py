import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(5)
elements=driver.find_elements(By.XPATH,"//div[@id='nav-xshop-container']/div/ul/li")
for element in elements:
    print(element.text)

