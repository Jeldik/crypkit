from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser.lower()

    def getWebDriverInstance(self):
        baseURL = "https://app2.crypkit.com/signup"

        if self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "ie":
            driver = webdriver.Ie()
        elif self.browser == "opera":
            driver = webdriver.Opera()
        else:
            driver = webdriver.Safari()

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get(baseURL)

        return driver
