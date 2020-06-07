import unittest
import pytest
import logging
from pages.signup_page import SignUpPage
from utilities.BaseClass import BaseClass


class SignUpTests(unittest.TestCase, BaseClass):

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.signUpPage = SignUpPage(self.driver)
        self.emptyData = self.signUpPage.loadEmptyData()
        self.validData = self.signUpPage.loadValidData()
        # self.logger = logging.getLogger(__name__)
        # self.fileHandler = logging.FileHandler("logfile.log")
        # self.logger.addHandler(self.fileHandler)
        # self.loggerName = inspect.stack()[1][3]
        # self.formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        # self.fileHandler.setFormatter(self.formatter)
        # self.logger.setLevel(logging.INFO)

    # Bez vyplnění zmáčknu sign up - dostanu 3 alerty
    @pytest.mark.run(order=1)
    def test_invalidSignUp(self):
        self.signUpPage.signUp(self.emptyData)

        result = self.signUpPage.verifySignUpFailed()

        assert result == True

    # Kladný průběh - vše vyplněno správně
    @pytest.mark.run(order=2)
    def test_validSignUp(self):
        self.driver.refresh()
        self.signUpPage.signUp(self.validData)

    # Nevalidní e-mail - očekávám error hlášku
    @pytest.mark.run(order=3)
    def test_third_case(self):
        print("order 3")

    # Heslo méně jak 8 - očekávám hlášku
    def test_pswLessThanEightChar(self):
        print("Heslo méně jak 8 znaků")

    def test_psw_less_than_eight_numbers(self):
        print("Less than 8 numbers")

    def test_psw_more_than_eight_char(self):
        print("neočekávám error")

    def test_psw_more_than_eight_numbers(self):
        print("neočekávám error")

    def test_different_passwords(self):
        print("očekávám error")

    def test_same_paswords(self):
        print("Heslo je stejné, neočekávám error message")

    def test_logo(self):
        print("Když kliknu na logo, měl bych se dostat na HP")

    def test_sign_in_here(self):
        print("Měl bych se dostat na stránku sign In")

    def test_policy(self):
        print("Když kliknu na policy, chci vidět policy")

    def test_getDriver(self):
        print("get Drivers by settings")

    @classmethod
    def tearDownClass(cls):
        print("I will run once after all tests")


if __name__ == '__main__':
    unittest.main()
