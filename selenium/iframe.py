import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/add-to-cart/")
driver.switch_to.frame('frame')
driver.find_element(By.ID,'firstName').send_keys('Nikhil')
driver.find_element(By.ID,"lastName").send_keys('B')


time.sleep(5)
driver.quit()

