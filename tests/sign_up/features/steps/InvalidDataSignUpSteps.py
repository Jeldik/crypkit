from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from BDDCommon.CommonSteps.webstepscommon import *
from pages.signup_page import SignUpPage


@when('I click on sign up')
def click_on_sign_up(context):
    context.driver.find_element(*SignUpPage.sign_up_button).click()


@then("I Should see three warning messages")
def see_three_warning_messages(context):
    emailErrorPresent = WebDriverWait(context.driver, 5).until(expected_conditions.presence_of_element_located(
        *config.ELEMENTCONFIG['email_error_message']))
    passwordErrorPresent = WebDriverWait(context.driver, 5).until(expected_conditions.presence_of_element_located(
        *config.ELEMENTCONFIG['password_error_message']))
    confirmErrorPresent = WebDriverWait(context.driver, 5).until(expected_conditions.presence_of_element_located(
        *config.ELEMENTCONFIG['password_confirm_error_message']))

    assert emailErrorPresent and passwordErrorPresent and confirmErrorPresent


@when("I type invalid e-mail format")
def type_invalid_email_format(context):
    context.driver.find_element(*config.ELEMENTCONFIG["email_field"]).send_keys(config.DATACONFIG["invalid_email"])
