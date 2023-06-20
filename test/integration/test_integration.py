import unittest

from main_penalty_calculate.penalty_calculate import PenaltyCalculate


class TestIntegration(unittest.TestCase):
    def test_evaluate_infractors(self):
        penalty_calculate = PenaltyCalculate(
            'Transit Ticket input 1.csv'
        )

        violators_avaliations = penalty_calculate.evaluate_infractors()

        self.assertEqual(
            violators_avaliations, [
                '467191153; Josevaldo Cal. O. Teiro; ARE-9420, KVI-2310; 26',
                '276787067; Osvaldo Plinio; BIO-9626; 5',
                '149178360; Gerusa Juventina; SOS-3257; 4'
            ]
        )
