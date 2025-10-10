from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/")
object = driver.find_element(By.LINK_TEXT, "Form Authentication")
action = webdriver.ActionChains(driver)
action.move_to_element(object).click().perform()
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.XPATH, "//button/i").click()
login_page=driver.find_element(By.XPATH, "//div[@id='flash']").text
assert "You logged into a secure area!" in login_page
driver.find_element(By.XPATH, "//a/i").click()
logout_page=driver.find_element(By.XPATH, "//div[@id='flash']").text
assert "You logged out of the secure area!" in logout_page
