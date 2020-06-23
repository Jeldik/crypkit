import logging as logger
from behave import *
import BDDCommon.CommonFuncs.webcommon as webcommon

logger.basicConfig(level="INFO")


@given("I go to the site {url}")
def go_to_url(context, url):
    logger.info("Navigation to the site: {}".format(url))
    context.driver = webcommon.go_to(url)
