import unittest

from main_penalty_calculate.models import (
    LicensePlate,
    IdentityCard,
    ViolatorAvaliation
)


class TestViolatorAvaliation(unittest.TestCase):
    def test_violator_avaliation_check_plates(self):
        violator_avaliation = ViolatorAvaliation(
            IdentityCard(
                '30.286.415-5',
                'Vonkuzi Amelnay'
            ),
            [
                LicensePlate(
                    'MVC-4848'
                ),
                LicensePlate(
                    'NEK-6986'
                ),
                LicensePlate(
                    'MXK-0463'
                )
            ]
        )

        license_plates_list = violator_avaliation.license_plate_numbers

        self.assertEqual(
            license_plates_list, [
                'MVC-4848',
                'NEK-6986',
                'MXK-0463'
            ]
        )
