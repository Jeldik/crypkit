from BDDCommon.CommonConfigs import config
from BDDCommon.CommonFuncs import webcommon


def before_scenario(context, scenario):
    # Otevřít browser
    context.driver = webcommon.open_browser()


def after_step(context, step):
    if step.status.name == 'failed':
        # take screen shot
        pass
