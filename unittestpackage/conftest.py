import pytest


@pytest.fixture(scope="class")
def setup(browser, osType):
    print("I will run once")

    selected_browser = switch_browser(browser)
    # new driver by selected browser

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

def switch_browser(argument):
    switcher = {
        "chrome": "chrome",
        "firefox": "firefox",
        "ie": "ie",
        "safari": "safari"
    }
    return switcher.get(argument, "Invalid argument")