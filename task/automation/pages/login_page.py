from selenium.webdriver.common.by import By

from Incubation.task.automation.pages.base_page import BasePage


class LoginPage(BasePage):
    FORM_AUTH_LINK = (By.LINK_TEXT, "Form Authentication")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.radius")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".flash.success")

    def open_login_page(self, base_url):
        self.driver.get(base_url)
        self.click(self.FORM_AUTH_LINK)

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
