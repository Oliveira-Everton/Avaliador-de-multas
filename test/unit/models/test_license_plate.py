import unittest

from main_penalty_calculate.models import LicensePlate


class TestLicensePlate(unittest.TestCase):
    def test_license_plate_number(self):
        license_plate = LicensePlate('QBJ-6840')

        plate_number = license_plate.number

        self.assertEqual(plate_number, 'QBJ-6840')
