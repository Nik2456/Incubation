import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/javascript-popup/")
driver.find_element(By.XPATH,"//button[.='Click ']").click()
alert= driver.switch_to.alert
alert_text = alert.text
print(f"Alert message: {alert_text}")
alert.accept()

time.sleep(5)
driver.close()