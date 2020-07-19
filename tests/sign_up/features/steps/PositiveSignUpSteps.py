from behave import *

from BDDCommon.CommonConfigs import config


@when("I fill valid form")
def fill_valid_form(context):
    context.driver.find_element(*config.ELEMENTCONFIG["first name"]).send_keys(config.DATACONFIG['first name'])
    context.driver.find_element(*config.ELEMENTCONFIG["last name"]).send_keys(config.DATACONFIG['last name'])
    context.driver.find_element(*config.ELEMENTCONFIG["email"]).send_keys(config.DATACONFIG['valid email'])
    context.driver.find_element(*config.ELEMENTCONFIG["password"]).send_keys(config.DATACONFIG['valid email'])
    context.driver.find_element(*config.ELEMENTCONFIG["confirm password"]).send_keys(config.DATACONFIG['valid email'])


@then("I should navigate to next page")
def navigate_next_page(context):
    pass
