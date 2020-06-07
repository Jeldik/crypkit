import pytest


@pytest.mark.usefixtures("oneTimeSetup", "loadValidData", "loadEmptyData")
class BaseClass:
    pass
