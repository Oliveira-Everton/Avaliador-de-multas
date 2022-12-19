import unittest

from penalty_calculate.models.license_plates import LicensePlates


class TestLicensePlates(unittest.TestCase):
    def test_check_plates(self):
        license_plates = LicensePlates(["KVX-9666", "ARE-9986"])

        check_plates = license_plates.check_plates()

        self.assertEqual(
            check_plates,
            ["KVX-9666", "ARE-9986"]
        )

    def test_add_plate(self):
        license_plates = LicensePlates(["HGH-5702", "BWR-1036"])

        license_plates.add_plate("RUH-6896")

        self.assertEqual(
            license_plates.check_plates(),
            ["HGH-5702", "BWR-1036", "RUH-6896"]
        )
