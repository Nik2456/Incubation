from datetime import datetime

import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    config.option.html_path = f"{report_dir}/report_{now}.html"

@pytest.fixture(scope='session', autouse = True)
def setup_teardown():
    print("Start")
    yield
    print("End")