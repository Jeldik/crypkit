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
        raise Exception("The browser type '{}' is not supported" .format(browser))

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
