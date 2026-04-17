import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/drag-and-drop/")
actions = ActionChains(driver)
drag=driver.find_element(By.ID,'drag2')
drop=driver.find_element(By.ID,'div2')
actions.drag_and_drop(drag,drop).perform()
time.sleep(2)
driver.refresh()
time.sleep(2)
drag1=driver.find_element(By.ID,'drag6')
drop1=driver.find_element(By.ID,'div2')
actions.drag_and_drop(drag1,drop1).perform()


time.sleep(5)
driver.quit()

