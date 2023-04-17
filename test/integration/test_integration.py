import unittest

from main_penalty_calculate.penalty_calculate import PenaltyCalculate


class TestIntegration(unittest.TestCase):
    def test_penalty_calculate_csv_reader(self):
        penalty_calculate = PenaltyCalculate("Transit Ticket input 1.csv")

        identity_cards_and_license_plate = penalty_calculate.csv_reader()

        self.assertEqual(
            identity_cards_and_license_plate, [
                '467191153; Josevaldo Cal. O. Teiro; ARE-9420; Gravíssima;' +
                ' 1999-11-05 15:00:00;' +
                ' 2000-01-25 10:00:00;' +
                ' ',
                '467191153; Josevaldo Cal. O. Teiro; KVI-2310; Gravíssima;' +
                ' 2000-01-01 15:00:00;' +
                ' 2000-01-04 10:00:00;' +
                ' ',
                '467191153; Josevaldo Cal. O. Teiro; KVI-2310; Grave;' +
                ' 2000-01-04 15:00:00;' +
                ' 2000-01-05 10:00:00;' +
                ' ',
                '467191153; Josevaldo Cal. O. Teiro; ARE-9420; Gravíssima;' +
                ' 2000-01-10 15:00:00;' +
                ' 2000-01-25 10:00:00;' +
                ' ',
                '276787067; Osvaldo Plinio; BIO-9626; Grave;' +
                ' 2000-02-05 14:00:00;' +
                ' 2000-02-10 11:00:00;' +
                ' ',
                '149178360; Gerusa Juventina; SOS-3257; Média;' +
                ' 2000-08-16 16:00:00;' +
                ' 2000-02-11 12:00:00;' +
                ' '
            ]
        )
