import pytest
from base.webdriverfactory import WebDriverFactory


@pytest.fixture(scope="class")
def oneTimeSetup(request):
    browser = request.config.getoption("--browser")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    # Pokud je fixture volaná třídou, třída bude mít na sobě nový atribut driver
    if request.cls is not None:
        request.cls.driver = driver

    yield
    driver.quit()


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


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

