from behave import *
from selenium.webdriver.support import expected_conditions
from BDDCommon.CommonSteps.webstepscommon import *


@then("I Should see three warning messages")
def see_three_warning_messages(context):
    emailErrorPresent = WebDriverWait(context.driver, 5).until(expected_conditions.presence_of_element_located(
        *config.ELEMENTCONFIG['email_error_message']))
    passwordErrorPresent = WebDriverWait(context.driver, 5).until(expected_conditions.presence_of_element_located(
        *config.ELEMENTCONFIG['password_error_message']))
    confirmErrorPresent = WebDriverWait(context.driver, 5).until(expected_conditions.presence_of_element_located(
        *config.ELEMENTCONFIG['password_confirm_error_message']))

    assert emailErrorPresent and passwordErrorPresent and confirmErrorPresent


@when("I type {element} format")
def type_invalid_email_format(context, element):
    context.driver.find_element(*config.ELEMENTCONFIG["email"]).send_keys(config.DATACONFIG[element])


@step("I type {element}")
def type_password(context, element):
    if 'confirm password' in element:
        context.driver.find_element(*config.ELEMENTCONFIG["confirm password"]).send_keys(config.DATACONFIG[element])
    else:
        context.driver.find_element(*config.ELEMENTCONFIG["password"]).send_keys(
            config.DATACONFIG[element])

