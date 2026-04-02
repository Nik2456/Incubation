import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/x-path/")
driver.find_element(By.ID,'FirstName').send_keys('Shaurya')
driver.find_element(By.XPATH,"//input[@type='LastName']").send_keys('India')
driver.find_element(By.CSS_SELECTOR,"input[class='MiddleName form-control']").send_keys('Middle')
driver.find_element(By.XPATH,"//textarea[@class='work-place-address form-control']").send_keys('work')
driver.find_element(By.XPATH,"(//div[@class='form-group'])[5]/textarea").send_keys('Home')
driver.find_element(By.XPATH,"(//div[@class='form-group'])[6]/input").send_keys('Personal Email')
driver.find_element(By.ID,"Corporate-email").send_keys('Corporate Email')
driver.find_element(By.ID,"tel").send_keys('555-555-5555')

time.sleep(5)
driver.quit()

