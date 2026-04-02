from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.msn.com/en-in")

wait = WebDriverWait(driver, 20)

# Wait for shadow host
shadow_host = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "super-nav"))
)

# Access shadow root
sr1 = shadow_host.shadow_root

# Next shadow
sr2 = sr1.find_element(By.CSS_SELECTOR, "#nav").shadow_root

# Get menu items
menu_items = sr2.find_elements(By.CSS_SELECTOR, "a")

for item in menu_items:
    text = item.text.strip()
    if text:
        print(text)