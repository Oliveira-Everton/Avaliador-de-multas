import unittest

from main_penalty_calculate.penalty_calculate import PenaltyCalculate


class TestIntegration(unittest.TestCase):
    def test_evaluate_infractors(self):
        penalty_calculate = PenaltyCalculate('Transit Ticket input 1.csv')

        violators_avaliations = penalty_calculate.evaluate_infractors()

        self.assertEqual(
            violators_avaliations,
            '467191153; Josevaldo Cal. O. Teiro; ARE-9420, KVI-2310; 19;' +
            ' 1075.64\n'
            '276787067; Osvaldo Plinio; BIO-9626; 5; 195.23\n'
            '149178360; Gerusa Juventina; SOS-3257; 4; 130.16'
        )

    def test_evaluate_infractors_with_invalid_demerit_points(self):
        penalty_calculate = PenaltyCalculate(
            'test/fixtures/Transit Ticket input 2.csv'
        )

        violators_avaliations = penalty_calculate.evaluate_infractors()

        self.assertEqual(
            violators_avaliations,
            '375944035; Dtcv. Olivera; QBJ-6840; 0; 293.47'
        )

    def test_evaluate_infractors_aggregate_penalty_amount(self):
        penalty_calculate = PenaltyCalculate(
            'test/fixtures/Transit Ticket input 3.csv'
        )

        violators_avaliations = penalty_calculate.evaluate_infractors()

        self.assertEqual(
            violators_avaliations, '138469945; Morgan; MGN-9130; 8; 283.61'
        )
