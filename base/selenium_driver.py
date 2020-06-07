

class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver

    def isElementPresent(self, locator):

        element = self.driver.find_element(*locator)

        if element is not None:
            return True
        else:
            return False
