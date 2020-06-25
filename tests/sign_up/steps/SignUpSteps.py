from BDDCommon.CommonSteps.webstepscommon import *


@step("User click on {element}")
def step_impl(context, element):
    """
    Step to
    :return:
    """
    print("passed")


@then("Should see three warning messages")
def step_impl(context):
    """
    Step to
    :return:
    """
    print("passed")


@when("User fill valid form")
def step_impl(context):
    """
    Step to
    :return:
    """
    print("passed")


@step("User get to {element} page")
def step_impl(context, element):
    """
    Step to
    :return:
    """
    print("passed")


@when("User type invalid format e-mail")
def step_impl(context):
    """
    Step to
    :return:
    """
    print("passed")


@then("Should see the {element} warning text")
def step_impl(context, element):
    """
    Step to
    :return:
    """
    print("passed")


@when("User type short password")
def step_impl(context):
    """
    Step to
    :return:
    """
    print("passed")


@when("User type valid password")
def step_impl(context):
    """
    Step to
    :return:
    """
    print("passed")


@then("User don't see warning message")
def step_impl(context):
    """
    Step to
    :return:
    """
    print("passed")


@when("User type password")
def step_impl(context):
    """
    Step to
    :return:
    """
    print("passed")


@step("User type different password")
def step_impl(context):
    """
    Step to type different password than previous password
    :return:
    """
    print("passed")


@when("User type in valid password")
def step_impl(context):
    """
    Step to type valid password
    :return:
    """
    print("passed")


@step("User type in same password")
def step_impl(context):
    """
    Step to type same passwrod as in previous step
    :return:
    """
    print("passed")


@then("User shouldn't see any warning text")
def step_impl(context):
    """
    Step to check that user not see any warning text
    :return:
    """
    print("passed")


@given("User visited sign up page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given User visited sign up page')