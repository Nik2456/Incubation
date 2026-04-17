import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/horizontal-scrolling/")
time.sleep(5)
#driver.execute_script("window.scrollBy(10000,0);")
driver.execute_script("window.scrollTo(document.body.scrollWidth,0);")


time.sleep(5)
driver.quit()

