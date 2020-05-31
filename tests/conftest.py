import pytest
from base.webdriverfactory import WebDriverFactory


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def loadValidData():
    return {
        "first_name": "Jan",
        "last_name": "Novák",
        "email": "jan@novak.cz",
        "password": "jannovak",
        "password_confirm": "jannovak"
    }


@pytest.fixture
def loadEmptyData():
    return {
        "first_name": "",
        "last_name": "",
        "email": "",
        "password": "",
        "password_confirm": ""
    }
