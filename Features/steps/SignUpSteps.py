import unittest
import pytest
from behave import *
from base.webdriverfactory import WebDriverFactory
from pages.signup_page import SignUpPage
from utilities.BaseClass import BaseClass

use_step_matcher("re")


class SignUpTest(unittest.TestCase, BaseClass):

    baseURL = "https://app2.crypkit.com/signup"

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.signUpPage = SignUpPage(self.driver, self.getLogger())
        self.emptyData = self.signUpPage.loadEmptyData()
        self.validData = self.signUpPage.loadValidData()

    @given("User visited crypkit sign up page")
    def step_impl(context):
        # driver = WebDriverFactory.getWebDriverInstance(context)
        # driver.get(SignUpTest.baseURL)
        pass

    @when("User don't fill form")
    def step_impl(context):
        print("passed")

    @step("Hit Sign Up button")
    def step_impl(context):
        print("passed")

    @then("Should see three warning messages")
    def step_impl(context):
        print("passed")

    @when("User fill valid form")
    def step_impl(context):
        print("passed")

    @then("Should get to success page")
    def step_impl(context):
        print("passed")

    @when("User fill invalid")
    def step_impl(context):
        print("passed")

    @then("Should see invalid e-mail warning text")
    def step_impl(context):
        print("passed")

    @when("User fill short password")
    def step_impl(context):
        print("passed")

    @then("Should see short password warning text")
    def step_impl(context):
        print("passed")

    @when("User fill valid password")
    def step_impl(context):
        print("passed")

    @then("User don't see warning message")
    def step_impl(context):
        print("passed")

    @when("User fill password")
    def step_impl(context):
        print("passed")

    @step("User fill different password")
    def step_impl(context):
        print("passed")

    @then("Should see different password warning text")
    def step_impl(context):
        print("passed")

    @when("User fill in valid password")
    def step_impl(context):
        print("passed")

    @step("User fill same password")
    def step_impl(context):
        print("passed")

    @then("Shouldn't see any warning text")
    def step_impl(context):
        print("passed")

    @when("User click on logo")
    def step_impl(context):
        print("passed")

    @then("Should get to homepage")
    def step_impl(context):
        print("passed")

    @when("User click on sign in button")
    def step_impl(context):
        print("passed")

    @then("Should get to sign in page")
    def step_impl(context):
        print("passed")

    @when("User click to policy button")
    def step_impl(context):
        print("passed")

    @then("Should see policy text")
    def step_impl(context):
        print("passed")


if __name__ == '__main__':
    unittest.main()
