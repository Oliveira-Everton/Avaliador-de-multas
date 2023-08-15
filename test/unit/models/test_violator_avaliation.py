import unittest

from main_penalty_calculate.models import IdentityCard, ViolatorAvaliation


class TestViolatorAvaliation(unittest.TestCase):
    def test_license_plate_numbers(self):
        violator_avaliation = ViolatorAvaliation(
            identity_card=IdentityCard('30.286.415-5', 'Vonkuzi Amelnay'),
            license_plates=['MVC-4848', 'NEK-6986', 'MXK-0463'],
            demerit_points=5,
            penalty_amount=88.38
        )

        license_plates_numbers = violator_avaliation.license_plate_numbers

        self.assertEqual(
            license_plates_numbers, ['MVC-4848', 'NEK-6986', 'MXK-0463']
        )

    def test_demerit_points(self):
        violator_avaliation = ViolatorAvaliation(
            identity_card=IdentityCard('30.286.415-5', 'Vonkuzi Amelnay'),
            license_plates=['MVC-4848', 'NEK-6986', 'MXK-0463'],
            demerit_points=5,
            penalty_amount=88.38
        )

        demerit_points = violator_avaliation.demerit_points

        self.assertEqual(demerit_points, 5)

    def test_sum_demerit_points(self):
        violator_avaliation = ViolatorAvaliation(
            identity_card=IdentityCard('30.286.415-5', 'Vonkuzi Amelnay'),
            license_plates=['MVC-4848', 'NEK-6986', 'MXK-0463'],
            demerit_points=5,
            penalty_amount=88.38
        )

        violator_avaliation.sum_demerit_points(3)

        total_demerit_points = violator_avaliation.demerit_points
        self.assertEqual(total_demerit_points, 8)

    def test_penalty_amount(self):
        violator_avaliation = ViolatorAvaliation(
            identity_card=IdentityCard('30.286.415-5', 'Vonkuzi Amelnay'),
            license_plates=['MVC-4848', 'NEK-6986', 'MXK-0463'],
            demerit_points=5,
            penalty_amount=88.38
        )

        penalty_amount = violator_avaliation.penalty_amount

        self.assertEqual(penalty_amount, 88.38)
