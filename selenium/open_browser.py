import time

import requests
from selenium import webdriver


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.google.com")
time.sleep(2)
