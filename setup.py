from setuptools import setup

setup(name="Python BDD framework",
      version="1.0",
      description="Python BDD framework",
      author="Tomas Jelinek",
      author_email="tomas.jelinek@gmail.com",
      packages=[
          "BDDCommon",
          "BDDCommon.CommonFuncs",
          "BDDCommon.CommonSteps",
      ],
      )
