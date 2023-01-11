import unittest

from penalty_calculate.models.license_plate import LicensePlate


class TestLicensePlate(unittest.TestCase):
    def test_property_license_plate(self):
        license_plate = LicensePlate("QBJ-6840")

        plate_number = license_plate.number

        self.assertEqual(plate_number, "QBJ-6840")
