import unittest

from main_penalty_calculate.models import IdentityCard, ViolatorAvaliation


class TestViolatorAvaliation(unittest.TestCase):
    def test_license_plate_numbers(self):
        violator_avaliation = ViolatorAvaliation(
            identity_card=IdentityCard('30.286.415-5', 'Vonkuzi Amelnay'),
            license_plates=['MVC-4848', 'NEK-6986', 'MXK-0463']
        )

        license_plates_list = violator_avaliation.license_plate_numbers

        self.assertEqual(
            license_plates_list, ['MVC-4848', 'NEK-6986', 'MXK-0463']
        )
