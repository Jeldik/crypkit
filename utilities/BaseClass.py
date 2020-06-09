import inspect
import logging

import pytest


@pytest.mark.usefixtures("oneTimeSetup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(fileHandler)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)

        return logger
