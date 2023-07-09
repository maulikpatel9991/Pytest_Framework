import pytest
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Config.read_data import read_csv_data

FAILURES_FILE = Path() / "Reports/failures.txt"
PASSES_FILE = Path() / "Reports/success.txt"
SCREENSHOT_FILE = Path() / "Reports/screenshot"
GRAPH_FILE = Path() / "Reports/Graph/"


def pytest_addoption(parser: str):
    """
    :param parser: {str}
    """
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="function")
def function_fixture() -> str:
    return "function fixture data"


@pytest.fixture(scope="class")
def class_fixture() -> str:
    """
    class Scope Fixture
    """
    return "class fixture data"


@pytest.fixture(scope="module")
def module_fixture() -> str:
    """
    Module scope fixture
    """
    return "module fixture data"


@pytest.fixture(scope="session")
def session_fixture() -> str:
    return "session fixture data"

@pytest.fixture(scope='class')
def use_get_driver(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://practicetestautomation.com/practice-test-login/")
        request.cls.driver = driver
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get("https://practicetestautomation.com/practice-test-login/")
        request.cls.driver = driver
    else:
        print("invalid Browser Name")
    yield driver

    def teardown_fixture():
        driver.quit()
    request.addfinalizer(teardown_fixture)


@pytest.fixture
def read_csv(request):
    """
    This method will be use read data from csv file.
    """
    csv_file_name = request.param
    return read_csv_data(csv_file_name)
