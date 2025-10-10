from Incubation.task.automation.pages.login_page import LoginPage
from Incubation.task.automation.pages.secure_page import SecurePage


def test_login_logout(driver, config):
    login_page = LoginPage(driver)
    secure_page = SecurePage(driver)

    login_page.open_login_page(config["base_url"])

    login_page.login(config["username"], config["password"])

    message = login_page.get_success_message()
    assert "You logged into a secure area!" in message
    print("✅ Login successful!")

    secure_page.logout()

    logout_message = secure_page.get_logout_message()
    assert "You logged out of the secure area!" in logout_message
    print("✅ Logout successful!")
