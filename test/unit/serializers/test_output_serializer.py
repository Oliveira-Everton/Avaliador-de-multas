import unittest

from main_penalty_calculate.models import ViolatorAvaliation, IdentityCard
from main_penalty_calculate.serializers import OutputSerializer


class TestOutputSerializer(unittest.TestCase):
    def test_output_string(self):
        violators_avaliations = [
            ViolatorAvaliation(
                identity_card=IdentityCard('29.441.369-8', 'Aoki'),
                license_plates=['UCH-6237'],
                demerit_points=4
            ),
            ViolatorAvaliation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plates=['IDE-3516'],
                demerit_points=7
            )
        ]

        output_string = OutputSerializer(violators_avaliations).output_string()

        self.assertEqual(
            output_string, [
                '29.441.369-8; Aoki; UCH-6237; 4',
                '19.632.142-6; Takashi; IDE-3516; 7'
            ]
        )

    def test_output_string_with_more_license_plates_in_same_identity_card(
        self
    ):
        violators_avaliations = [
            ViolatorAvaliation(
                identity_card=IdentityCard('29.441.369-8', 'Aoki'),
                license_plates=['UCH-6237', 'HUG-2023'],
                demerit_points=7
            )
        ]

        output_string = OutputSerializer(violators_avaliations).output_string()

        self.assertEqual(
            output_string, [
                '29.441.369-8; Aoki; UCH-6237, HUG-2023; 7'
            ]
        )
