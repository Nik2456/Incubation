import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/dropdown/")
driver.find_element(By.XPATH,"(//span[.='Select Choice 3'])[1]").click()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("Power11")


time.sleep(5)
driver.close()