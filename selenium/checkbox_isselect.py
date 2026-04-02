import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/is-selected/")
check_box=driver.find_element(By.XPATH,"(//input[@id='vehicle2'])[3]")
#check_box1=driver.find_element(By.XPATH,"(//input[@id='vehicle2'])[4]")
check_box.click()
assert check_box.is_selected()
#assert check_box1.is_selected()

time.sleep(5)
driver.close()