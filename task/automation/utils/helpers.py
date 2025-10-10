import os
from datetime import datetime

def capture_screenshot(driver, name_prefix="failure"):
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(folder, f"{name_prefix}_{timestamp}.png")
    driver.save_screenshot(filename)
    print(f"📸 Screenshot saved: {filename}")
