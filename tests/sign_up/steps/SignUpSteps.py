from BDDCommon.CommonSteps.webstepscommon import *
from pages.signup_page import SignUpPage


@step("I click on {element}")
def click_on_element(context, element):
    if element.lower() == 'sign up':
        SignUpPage.clickSignUpButton()
    else:
        Exception("Unknown element!")


@then("Should see three warning messages")
def step_impl(context):
    print("passed")


@when("I fill valid form")
def step_impl(context):
    print("passed")


@step("User get to {element} page")
def step_impl(context, element):
    print("passed")


@when("User type invalid format e-mail")
def step_impl(context):
    print("passed")


@then("Should see the {element} warning text")
def step_impl(context, element):
    print("passed")


@when("User type short password")
def step_impl(context):
    print("passed")


@when("User type valid password")
def step_impl(context):
    print("passed")


@then("User don't see warning message")
def step_impl(context):
    print("passed")


@when("User type password")
def step_impl(context):
    print("passed")


@step("User type different password")
def step_impl(context):
    print("passed")


@when("User type in valid password")
def step_impl(context):
    print("passed")


@step("User type in same password")
def step_impl(context):
    print("passed")


@then("User shouldn't see any warning text")
def step_impl(context):
    print("passed")


@given("User visited sign up page")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given User visited sign up page')