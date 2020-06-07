from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver

    def isElementPresent(self, locator):
        element = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))

        if element is not None:
            return True
        else:
            return False
