import unittest

from main_penalty_calculate.models import (
    ViolatorAvaliation,
    IdentityCard,
    LicensePlate,
)
from main_penalty_calculate.serializers import OutputSerializer


class TestOutputSerializer(unittest.TestCase):
    def test_output_serializer_output_string(self):
        first_violator_avaliation = ViolatorAvaliation(
            identity_card=IdentityCard('29.441.369-8', 'Aoki'),
            license_plates=[
                LicensePlate('UCH-6237')
            ]
        )
        second_violator_avaliation = ViolatorAvaliation(
            identity_card=IdentityCard('19.632.142-6', 'Takashi'),
            license_plates=[
                LicensePlate('IDE-3516')
            ]
        )
        violators_avaliations = [
            first_violator_avaliation, second_violator_avaliation
        ]

        output_string = OutputSerializer(violators_avaliations).output_string()

        self.assertEqual(
            output_string, [
                '29.441.369-8; Aoki; UCH-6237',
                '19.632.142-6; Takashi; IDE-3516'
            ]
        )
