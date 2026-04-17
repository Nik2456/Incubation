import time

from selenium import webdriver

from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/nested-frame/")
driver.switch_to.frame("outerIframe")
driver.switch_to.frame("inner frame")
driver.find_element(By.ID,"Email").send_keys("abc@abc.com")

time.sleep(5)
driver.quit()

