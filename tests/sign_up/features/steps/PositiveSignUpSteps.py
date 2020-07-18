from behave import *

from BDDCommon.CommonConfigs import config


@when("I fill valid form")
def fill_valid_form(context):
    context.driver.find_element(*config.ELEMENTCONFIG["first_name_field"]).send_keys(config.DATACONFIG['first_name'])
    context.driver.find_element(*config.ELEMENTCONFIG["last_name_field"]).send_keys(config.DATACONFIG['last_name'])
    context.driver.find_element(*config.ELEMENTCONFIG["email_field"]).send_keys(config.DATACONFIG['valid_email'])
    context.driver.find_element(*config.ELEMENTCONFIG["password_field"]).send_keys(config.DATACONFIG['valid_email'])
    context.driver.find_element(*config.ELEMENTCONFIG["password_confirm_field"]) \
        .send_keys(config.DATACONFIG['valid_email'])


@then("I should navigate to next page")
def navigate_next_page(context):
    pass
