from selenium import webdriver


def go_to(url, browser=None):
    if not browser or browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser.lower() == "ie":
        driver = webdriver.Ie()
    elif browser.lower() == "opera":
        driver = webdriver.Opera()
    elif browser.lower() == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception("The browser type '{}' is not supported".format(browser))

    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.delete_all_cookies()

    url = url.strip()
    driver.get(url)

    return driver


def assert_text_visible(text):
    pass


def assert_element_visible(element):
    pass


def assert_page_title(context, expected_title):
    actual_title = context.driver.title

    assert expected_title == actual_title, "The title is not as expected." \
                                           " Expected: {}, Actual: {}".format(expected_title, actual_title)


def assert_current_url(context, expected_url):
    current_url = context.driver.url

    assert expected_url == current_url, "The current url is not as expected." \
                                        " Expected: {}, Actual: {}".format(expected_url, current_url)


