import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/vertical-scrolling/")
driver.execute_script("window.scrollBy(0,2000);")
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


time.sleep(5)
driver.quit()

