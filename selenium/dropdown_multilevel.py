import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://grotechminds.com/multi-level-dropdown/")

wait = WebDriverWait(driver, 10)

# Step 1: Click outer dropdown
outer_dropdown = wait.until(
    EC.element_to_be_clickable((By.ID, "outer-dropdown"))
)
outer_dropdown.click()

# Step 2: Select an option from outer dropdown
outer_option = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//li[text()='Option 4']"))
)
outer_option.click()

# Step 3: Click inner dropdown (appears after outer selection)
inner_dropdown = wait.until(
    EC.element_to_be_clickable((By.ID, "inner-dropdown"))
)
inner_dropdown.click()

# Step 4: Select option from inner dropdown
inner_option = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//li[text()='Option 2']"))
)
inner_option.click()

time.sleep(5)
driver.quit()