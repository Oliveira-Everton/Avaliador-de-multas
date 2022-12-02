import unittest

from penalty_calculate.managers.file_manager import FileManager


class TestFileManager(unittest.TestCase):

    def test_take_national_identity_cards(self):
        file = FileManager("Transit Ticket input 1.csv")

        take_national_name_and_number_identity_cards = file.take_national_identity_cards()
        

        self.assertEqual(
            take_national_name_and_number_identity_cards,
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
        file = FileManager("Transit Ticket input 1.csv")

        take_license_plate = file.take_license_plate()

        self.assertEqual(take_license_plate, ["ARE-9420", "KVI-2310", "KVI-2310", "ARE-9420", "BIO-9626", "SOS-3257"])
