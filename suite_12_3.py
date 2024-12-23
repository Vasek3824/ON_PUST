import unittest
from unittest import TestSuite
import tests_12_3

test_suite = TestSuite()

test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTes))

runner = unittest.TextTestRunner(verbosity=5)
runner.run(test_suite)
