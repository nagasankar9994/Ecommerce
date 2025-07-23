import os
import re
import time

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browsername", action="store",default="chrome",help="Browser to run tests on: chrome or firefox"
    )
driver=None

@pytest.fixture(scope="function")
def browserInvoke(request):
    global driver
    browser_name=request.config.getoption("browsername")
    if browser_name=="chrome":
      driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
    elif browser_name =='edge':
        driver=webdriver.Edge()
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")#https://rahulshettyacademy.com/angularpractice/
    driver.maximize_window()
    yield driver
    time.sleep(2)
    driver.quit()

import os
import re
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ('call', 'setup'):
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Get WebDriver from fixture
            driver = item.funcargs.get("browserInvoke")  # Make sure your fixture is named correctly

            if driver:
                reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
                os.makedirs(reports_dir, exist_ok=True)

                # Safe filename
                safe_name = re.sub(r'[^\w\.]', '_', report.nodeid)
                file_name = os.path.join(reports_dir, f"{safe_name}.png")
                print("file name is", file_name)

                _capture_screenshot(driver, file_name)

                if os.path.exists(file_name):
                    html = (
                        f'<div><img src="{file_name}" alt="screenshot" '
                        f'style="width:304px;height:228px;" '
                        f'onclick="window.open(this.src)" align="right"/></div>'
                    )
                    extra.append(pytest_html.extras.html(html))

    report.extras = extra


def _capture_screenshot(driver, file_name):
    driver.get_screenshot_as_file(file_name)
