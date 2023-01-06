import unittest

from penalty_calculate.penalty_calculate import PenaltyCalculate


class TestIntegration(unittest.TestCase):

    def test_penalty_calculate(self):
        penalty_calculate = PenaltyCalculate("Transit Ticket input 1.csv")

        national_identity_cards_with_license_plate = penalty_calculate.csv_reader()

        self.assertEqual(
            national_identity_cards_with_license_plate, [
                '467191153; Josevaldo Cal. O. Teiro',
                '467191153; Josevaldo Cal. O. Teiro',
                '467191153; Josevaldo Cal. O. Teiro',
                '467191153; Josevaldo Cal. O. Teiro',
                '276787067; Osvaldo Plinio',
                '149178360; Gerusa Juventina',
                'ARE-9420', 'KVI-2310', 'KVI-2310',
                'ARE-9420', 'BIO-9626', 'SOS-3257'
            ]
        )
