import logging as logger
from behave import *
import BDDCommon.CommonFuncs.webcommon as webcommon

logger.basicConfig(level="INFO")


@given("I go to the site {url}")
def go_to_url(context, url):
    logger.info("Navigation to the site: {}".format(url))
    context.driver = webcommon.go_to(url)


@then("the page title should be {expected_title}")
def verify_homepage_title(context, expected_title):
    webcommon.assert_page_title(expected_title)


@then("current url should be {expected_url}")
def verify_current_url(context, expected_url):
    webcommon.assert_current_url(context, expected_url)
