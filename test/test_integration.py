import unittest

from penalty_avaliator.penalty_calculate import PenaltyCalculate

class TestIntegration(unittest.TestCase):
    def test_penalty_calculate(self):
        penalty_calculate = PenaltyCalculate()

        result = penalty_calculate.calculate_penalty()

        self.assertEqual(result, True)
