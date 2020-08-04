from BDDCommon.CommonConfigs import config
from BDDCommon.CommonFuncs import webcommon


def before_scenario(context, scenario):
    # Otevřít browser
    # jít na testovanou stránku
    # url = config.URLCONFIG['sign up']
    url = 'www.seznam.cz'
    context.driver = webcommon.go_to(url)
