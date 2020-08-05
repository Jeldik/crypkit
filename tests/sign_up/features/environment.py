from BDDCommon.CommonConfigs import config
from BDDCommon.CommonFuncs import webcommon


def before_scenario(context, scenario):
    # Otevřít browser
    # jít na testovanou stránku
    # url = config.URLCONFIG['sign up']
    context.driver = webcommon.open_browser()


def after_step(context, step):
    if step.status.name == 'failed':
        # take screen shot
        pass
