import unittest

from penalty_calculate.penalty_calculate import PenaltyCalculate


class TestIntegration(unittest.TestCase):
    def test_penalty_calculate_csv_reader(self):
        penalty_calculate = PenaltyCalculate("Transit Ticket input 1.csv")

        identity_cards_and_license_plate = penalty_calculate.csv_reader()

        self.assertEqual(
            identity_cards_and_license_plate, [
                '467191153; Josevaldo Cal. O. Teiro; ARE-9420',
                '467191153; Josevaldo Cal. O. Teiro; KVI-2310',
                '467191153; Josevaldo Cal. O. Teiro; KVI-2310',
                '467191153; Josevaldo Cal. O. Teiro; ARE-9420',
                '276787067; Osvaldo Plinio; BIO-9626',
                '149178360; Gerusa Juventina; SOS-3257'
            ]
        )
