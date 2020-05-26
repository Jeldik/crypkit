

class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver

    def isElementPresent(self, locator, locatorType="id"):
        locatorType = locatorType.lower()

        if locatorType == "id":
            element = self.driver.find_element_by_id(locator)
        elif locatorType == "name":
            element = self.driver.find_element_by_name(locator)
        elif locatorType == "xpath":
            element = self.driver.find_element_by_xpath(locator)
        elif locatorType == "css":
            element = self.driver.find_element_by_css_selector(locator)
        elif locatorType == "linktext":
            element = self.driver.find_element_by_link_text(locator)

        if element is not None:
            return True
        else:
            return False
