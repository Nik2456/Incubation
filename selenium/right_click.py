import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/rightclick/")
actions = ActionChains(driver)
right_click_button=driver.find_element(By.LINK_TEXT, "Practice Link2")

actions.context_click(right_click_button).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()



time.sleep(5)
driver.close()