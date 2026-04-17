import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/window-handle-and-handles/")
driver.find_element(By.XPATH,"(//button[.='Launch Tab2'])[1]").click()
window_open=driver.window_handles
print(window_open)
driver.switch_to.window(window_open[-1])
driver.maximize_window()

driver.find_element(By.ID,'APjFqb').send_keys('India')
time.sleep(5)
driver.close()
driver.switch_to.window(window_open[0])
driver.find_element(By.XPATH,"(//button[.='Launch Broweser 2'])[1]").click()


time.sleep(5)
driver.quit()
