import pytest


@pytest.mark.usefixtures('setup_browser')
class TestGoogle:
    def test_open_google(self):
        self.driver.get("https://www.google.com/")
        assert "Google" in self.driver.title

    def test_search(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element("name", "q")
        search_box.send_keys("India")
        search_box.submit()
        assert "India" in self.driver.page_source