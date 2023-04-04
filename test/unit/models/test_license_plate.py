import unittest

from main_penalty_calculate.models import LicensePlate


class TestLicensePlate(unittest.TestCase):
    def test_license_plate_number(self):
        license_plate = LicensePlate("QBJ-6840", "Grave")

        plate_number = license_plate.number

        self.assertEqual(plate_number, "QBJ-6840")

    def test_license_plate_type_infraction(self):
        license_plate = LicensePlate("BYE-1996", "Média")

        type_infraction = license_plate.type_infraction

        self.assertEqual(type_infraction, "Média")
