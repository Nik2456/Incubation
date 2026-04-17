import time

from selenium import webdriver

from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://grotechminds.com/web-tables/")
percentages=driver.find_elements(By.XPATH,"//tbody/tr/td[3]")
print(percentages)
count=0
for perc in percentages:
    text_value = perc.text.strip()

    if int(text_value)>86:
        count += 1

print(count)
time.sleep(5)
driver.quit()

