import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/hoverover/")
actions = ActionChains(driver)
element=driver.find_element(By.XPATH,"//div[@class='toolrip5']")
actions.move_to_element(element).perform()



time.sleep(5)
driver.close()