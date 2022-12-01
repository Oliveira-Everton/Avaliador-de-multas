import unittest

from penalty_calculate.managers.file_manager import FileManager

class TestIntegration(unittest.TestCase):
    def test_receive_file_and_evaluate(self):
        file = FileManager("Transit Ticket input 1.csv")
        
        take_national_identity_cards_with_license_plate = file.take_national_identity_cards_with_license_plate()

        self.assertEqual(
            take_national_identity_cards_with_license_plate, 
            [
                ["467191153", "Josevaldo Cal. O. Teiro"], 
                ["467191153", "Josevaldo Cal. O. Teiro"],
                ["467191153", "Josevaldo Cal. O. Teiro"],
                ["467191153", "Josevaldo Cal. O. Teiro"], 
                ["276787067", "Osvaldo Plinio"], 
                ["149178360", "Gerusa Juventina"],
                ["ARE-9420", "KVI-2310", "KVI-2310", "ARE-9420", "BIO-9626", "SOS-3257"]
            ]
        )
