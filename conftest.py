import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
from datetime import datetime

FAILURES_FILE = Path() / "Reports/failures.txt"
PASSES_FILE = Path() / "Reports/success.txt"
SCREENSHOT_FILE = Path() / "Reports/screenshot"
GRAPH_FILE = Path() / "Reports/Graph/"

@pytest.fixture(scope='function')
def driver_get(request):
    if request.param == 'firefox':
        get_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        get_driver.get("https://practicetestautomation.com/practice-test-login/")
        request.cls.driver1 = get_driver
        yield get_driver
        get_driver.quit()
    elif request.param == "chrome":
        get_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        get_driver.get("https://practicetestautomation.com/practice-test-login/")
        request.cls.driver1 = get_driver
        yield get_driver
        get_driver.quit()


"""
Pytest Hook 
All Hook pytestdebug.log
"""


def pytest_configure(config):
    config._metadata['Project Name'] = 'Demo'
    config._metadata['Module Name'] = 'maulik'
    config._metadata['Tester'] = 'Demo'


def pytest_sessionfinish(session):
    print("************************ pytest session finish Hook", session)


def pytest_html_report_title(report):
    report.title = "Maulik Patel Reports"


def pytest_runtest_setup(item):
    print("************************ pytest runtest setup Hook", item.name)


def pytest_sessionstart() -> None:
    """
    This method will be use check File is existing or not
    """
    if FAILURES_FILE.exists() and PASSES_FILE.exists():
        """
        We want to delete the file if it already exists
        """
        FAILURES_FILE.unlink()
        PASSES_FILE.unlink()
    """
    If the file already exists delete it, then create a new one.
    """
    FAILURES_FILE.touch()
    PASSES_FILE.touch()

@pytest.mark.hookwrapper
def pytest_runtest_makereport():
    outcome = yield
    result = outcome.get_result()
    """
    Here if the condition is true, print Fail test case Name
    if condition is false print Pass Test Case Name
    """
    if result.when == "call" and result.failed:
        try:
            with open(str(FAILURES_FILE), "a") as f:
                now = datetime.now()
                time = now.strftime("%d/%m/%y %I:%M:%S %p %A  ")
                result_file = str(time) + result.nodeid
                f.write(result_file + "\n")
        except Exception as error:
            print(error)
    elif result.when == "call" and result.passed:
        try:
            with open(str(PASSES_FILE), "a") as f:
                now = datetime.now()
                time = now.strftime("%d/%m/%y %I:%M:%S %p %A")
                result_file = str(time) + result.nodeid
                f.write(result_file + "\n")
        except Exception as error:
            print(error)

def graph(user_chart):
    with open(str(FAILURES_FILE), 'r') as fp:
        fail_count = len(fp.readlines())
        print('Total Number of lines:', fail_count)
    with open(str(PASSES_FILE), 'r') as fp:
        pass_count = len(fp.readlines())
        print('Total Number of lines:', pass_count)
    data_dict = {'TEST_TYPE': ['PASS', 'FAIL'],
                 'TEST': [pass_count, fail_count]
                 }
    df = pd.DataFrame(data_dict)
    df.head()
    df.plot(kind=user_chart,
            x='TEST_TYPE',
            y='TEST',
            color='green'
            )
    plt.title('TESTCASE')
    file_path = "{}/{}.graph.png".format(str(GRAPH_FILE), 1)
    plt.savefig(file_path)