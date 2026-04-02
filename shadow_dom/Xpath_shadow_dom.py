from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://watir.com/examples/shadow_dom.html")
shadow_root = driver.find_element(By.CSS_SELECTOR,"[id='shadow_host']").shadow_root
shadow_text = shadow_root.find_element(By.CSS_SELECTOR,"[id='shadow_content']").text
shadow_root2 = shadow_root.find_element(By.CSS_SELECTOR,"[id='nested_shadow_host']").shadow_root
shadow_text2 = shadow_root2.find_element(By.CSS_SELECTOR,"[id='nested_shadow_content']").text
print(shadow_text)
print(shadow_text2)

