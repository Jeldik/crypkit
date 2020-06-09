from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class SignUpPage:

    _base_url = "https://app2.crypkit.com/signup"

    first_name_field = (By.ID, "sign-up-first-name")
    last_name_field = (By.ID, "sign-up-last-name")
    email_field = (By.ID, "sign-up-email")
    password_field = (By.ID, "sign-up-password")
    password_confirm_field = (By.ID, "sign-up-password-confirm")
    sign_up_button = (By.ID, "sign-up-submit")
    email_error_message = (By.XPATH, "//*[@id=\'sign-up-form\']/span[1]/div/div/span")
    password_error_message = (By.XPATH, "//*[@id=\'sign-up-form\']/span[2]/div/div/span")
    password_confirm_message = (By.XPATH, "//*[@id=\'sign-up-form\']/span[3]/div/div/span")

    def __init__(self, driver, logger):
        self.driver = driver
        self.log = logger

    def getFirstNameField(self):
        return self.driver.find_element(*SignUpPage.first_name_field)

    def getLastNameField(self):
        return self.driver.find_element(*SignUpPage.last_name_field)

    def getEmailField(self):
        return self.driver.find_element(*SignUpPage.email_field)

    def getPasswordField(self):
        return self.driver.find_element(*SignUpPage.password_field)

    def getPasswordConfirmField(self):
        return self.driver.find_element(*SignUpPage.password_confirm_field)

    def getSignUpButton(self):
        return self.driver.find_element(*SignUpPage.sign_up_button)

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

    def signUp(self, data):
        self.enterFirstName(data["first_name"])
        self.enterLastName(data["last_name"])
        self.enterEmail(data["email"])
        self.enterPassword(data["password"])
        self.enterPasswordConfirm(data["password_confirm"])

        self.log.info("Vyplněna vstupní data: " + data["first_name"] + ", " + data["last_name"] + ", " + data["email"]
                      + ", " + data["password"])

        # FIXME před odevzdáním
        if len(data["first_name"]) == 0:
            self.clickSignUpButton()

    def verifySignUpFailed(self):
        seDriver = SeleniumDriver(self.driver)

        emailErrorPresent = seDriver.isElementPresent(locator=self.email_error_message)
        passwordErrorPresent = seDriver.isElementPresent(locator=self.password_error_message)
        confirmErrorPresent = seDriver.isElementPresent(locator=self.password_confirm_message)

        return emailErrorPresent and passwordErrorPresent and confirmErrorPresent

    def loadValidData(self):
        return {
            "first_name": "Jan",
            "last_name": "Novák",
            "email": "jan@novak.cz",
            "password": "jannovak",
            "password_confirm": "jannovak"
        }

    def loadEmptyData(self):
        return {
            "first_name": "",
            "last_name": "",
            "email": "",
            "password": "",
            "password_confirm": ""
        }

