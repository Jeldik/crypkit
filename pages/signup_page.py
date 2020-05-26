from base.selenium_driver import SeleniumDriver


class SignUpPage:

    def __init__(self, driver):
        self.driver = driver

    # locators
    _first_name_field = "sign-up-first-name"
    _last_name_field = "sign-up-last-name"
    _email_field = "sign-up-email"
    _password_field = "sign-up-password"
    _password_confirm_field = "sign-up-password-confirm"
    _sign_up_button = "sign-up-submit"
    _email_error_message = "//*[@id=\'sign-up-form\']/span[1]/div/div/span"
    _password_error_message = "//*[@id=\'sign-up-form\']/span[2]/div/div/span"
    _password_confirm_message = "//*[@id=\'sign-up-form\']/span[3]/div/div/span"
    _base_url = "https://app2.crypkit.com/signup"

    def getFirstNameField(self):
        return self.driver.find_element_by_id(self._first_name_field)

    def getLastNameField(self):
        return self.driver.find_element_by_id(self._last_name_field)

    def getEmailField(self):
        return self.driver.find_element_by_id(self._email_field)

    def getPasswordField(self):
        return self.driver.find_element_by_id(self._password_field)

    def getPasswordConfirmField(self):
        return self.driver.find_element_by_id(self._password_confirm_field)

    def getSignUpButton(self):
        return self.driver.find_element_by_id(self._sign_up_button)

    def clickSignUpButton(self):
        self.getSignUpButton().click()

    def enterFirstName(self, firstname=""):
        self.getFirstNameField().send_keys(firstname)

    def enterLastName(self, lastname=""):
        self.getLastNameField().send_keys(lastname)

    def enterEmail(self, email=""):
        self.getEmailField().send_keys(email)

    def enterPassword(self, password=""):
        self.getPasswordField().send_keys(password)

    def enterPasswordConfirm(self, passwordconfirm=""):
        self.getPasswordConfirmField().send_keys(passwordconfirm)

    def signUp(self, firstname="", lastname="", email="", password="", passwordconfirm=""):
        self.enterFirstName(firstname)
        self.enterLastName(lastname)
        self.enterEmail(email)
        self.enterPassword(password)
        self.enterPasswordConfirm(passwordconfirm)

        # FIXME před odevzdáním
        if len(firstname) == 0:
            self.clickSignUpButton()

    def refreshPage(self):
        self.driver.get(self._base_url)

    def verifySignUpFailed(self):
        seDriver = SeleniumDriver(self.driver)
        emailErrorPresent = seDriver.isElementPresent(locator=self._email_error_message, locatorType="xpath")
        passwordErrorPresent = seDriver.isElementPresent(locator=self._password_error_message, locatorType="xpath")
        confirmErrorPresent = seDriver.isElementPresent(locator=self._password_confirm_message, locatorType="xpath")

        return emailErrorPresent and passwordErrorPresent and confirmErrorPresent
