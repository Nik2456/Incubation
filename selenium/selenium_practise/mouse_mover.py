import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/mousemover/")
driver.find_element(By.LINK_TEXT,"DemoLink2").click()
window_open=driver.window_handles
driver.switch_to.window(window_open[-1])
driver.find_element(By.ID,'APjFqb').send_keys('India')

time.sleep(5)
driver.close()