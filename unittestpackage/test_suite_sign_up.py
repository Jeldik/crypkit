import unittest
from tests.signup_tests import TestSignUp

# Get all tests from test Class
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestSignUp)

smoke_test = unittest.TestSuite(tc1)

unittest.TextTestRunner().run(smoke_test)