import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/multiple-select/")
dropdown=Select(driver.find_element(By.ID,"automobiles"))
dropdown.select_by_index(0)
dropdown.select_by_value("sedan")
dropdown.select_by_visible_text("Hatchback")
dropdown.select_by_index(3)
dropdown.deselect_all()





time.sleep(5)
driver.quit()

