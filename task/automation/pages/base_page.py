from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator, text):
        field = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )
        field.clear()
        field.send_keys(text)

    def get_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text
