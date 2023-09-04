import unittest

from main_penalty_calculate.serializers import OutputSerializer
from main_penalty_calculate.models import (
    ViolatorAvaliation,
    IdentityCard,
    LicensePlate
)


class TestOutputSerializer(unittest.TestCase):
    def test_output_string(self):
        violators_avaliations = [
            ViolatorAvaliation(
                identity_card=IdentityCard('29.441.369-8', 'Aoki'),
                license_plates=[LicensePlate('UCH-6237')],
                demerit_points=4,
                penalty_amount=88.38
            ),
            ViolatorAvaliation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plates=[LicensePlate('IDE-3516')],
                demerit_points=7,
                penalty_amount=293.47
            )
        ]

        output_string = OutputSerializer(violators_avaliations).output_string()
        self.assertEqual(
            output_string,
            '29.441.369-8; Aoki; UCH-6237; 4; 88.38\n' +
            '19.632.142-6; Takashi; IDE-3516; 7; 293.47'
        )

    def test_output_string_with_more_license_plates_in_same_identity_card(
        self
    ):
        violators_avaliations = [
            ViolatorAvaliation(
                identity_card=IdentityCard('29.441.369-8', 'Aoki'),
                license_plates=[
                    LicensePlate('UCH-6237'), LicensePlate('HUG-2023')
                ],
                demerit_points=7,
                penalty_amount=293.47
            )
        ]

        output_string = OutputSerializer(violators_avaliations).output_string()

        self.assertEqual(
            output_string, '29.441.369-8; Aoki; UCH-6237, HUG-2023; 7; 293.47'
        )
