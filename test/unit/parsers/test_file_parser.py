import unittest

from penalty_calculate.parsers.file_parser import FileParser


class TestFileManager(unittest.TestCase):

    def test_take_national_identity_cards(self):
        csv_file = FileParser("Transit Ticket input 1.csv")

        take_national_identity_cards = csv_file.take_national_identity_cards()

        self.assertEqual(
            take_national_identity_cards,
            [
                ["467191153", "Josevaldo Cal. O. Teiro"],
                ["467191153", "Josevaldo Cal. O. Teiro"],
                ["467191153", "Josevaldo Cal. O. Teiro"],
                ["467191153", "Josevaldo Cal. O. Teiro"],
                ["276787067", "Osvaldo Plinio"],
                ["149178360", "Gerusa Juventina"]
            ]
        )

    def test_take_license_plate(self):
        csv_file = FileParser("Transit Ticket input 1.csv")

        take_license_plate = csv_file.take_license_plate()

        self.assertEqual(
            take_license_plate,
            ["ARE-9420", "KVI-2310", "KVI-2310",
                "ARE-9420", "BIO-9626", "SOS-3257"]
        )

    def test_take_national_identity_cards_with_license_plate(self):
        csv_file = FileParser("Transit Ticket input 1.csv")

        id_and_license_plate = csv_file.take_id_cards_with_license_plate()

        self.assertEqual(
            id_and_license_plate,
            [
                ["467191153", "Josevaldo Cal. O. Teiro"],
                ["467191153", "Josevaldo Cal. O. Teiro"],
                ["467191153", "Josevaldo Cal. O. Teiro"],
                ["467191153", "Josevaldo Cal. O. Teiro"],
                ["276787067", "Osvaldo Plinio"],
                ["149178360", "Gerusa Juventina"],
                ["ARE-9420", "KVI-2310", "KVI-2310",
                    "ARE-9420", "BIO-9626", "SOS-3257"]
            ]
        )
