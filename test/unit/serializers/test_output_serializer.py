import unittest

from main_penalty_calculate.models import (
    ViolatorAvaliation,
    IdentityCard,
    LicensePlates,
)
from main_penalty_calculate.serializers import OutputSerializer


class TestOutputSerializer(unittest.TestCase):
    def test_output_serializer_output_string(self):
        first_traffic_violation = ViolatorAvaliation(
            identity_card=IdentityCard('29.441.369-8', 'Aoki'),
            license_plates=LicensePlates('UCH-6237')
        )
        second_traffic_violation = ViolatorAvaliation(
            identity_card=IdentityCard('19.632.142-6', 'Takashi'),
            license_plates=LicensePlates('IDE-3516')
        )
        traffic_violations = [
            first_traffic_violation, second_traffic_violation
        ]

        output_string = OutputSerializer(traffic_violations).output_string()

        self.assertEqual(
            output_string, [
                '29.441.369-8; Aoki; UCH-6237',
                '19.632.142-6; Takashi; IDE-3516'
            ]
        )
