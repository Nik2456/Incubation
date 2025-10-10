from selenium.webdriver.common.by import By

from Incubation.task.automation.pages.base_page import BasePage


class SecurePage(BasePage):
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".flash.success")

    def logout(self):
        self.click(self.LOGOUT_BUTTON)

    def get_logout_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
