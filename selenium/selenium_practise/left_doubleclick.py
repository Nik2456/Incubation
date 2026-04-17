import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/left-double-click/")
actions = ActionChains(driver)
left_click_button=driver.find_element(By.XPATH, "//div[@class='popup2']")

actions.double_click(left_click_button).perform()



time.sleep(5)
driver.close()