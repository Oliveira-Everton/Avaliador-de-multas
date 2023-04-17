import unittest

from main_penalty_calculate.models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate,
)
from main_penalty_calculate.serializers import OutputSerializer


class TestOutputSerializer(unittest.TestCase):
    def test_output_serializer_output_string(self):
        first_traffic_violation = TrafficViolation(
            IdentityCard("22.193.598-8", "Ericka"),
            LicensePlate("QTB-0067")
        )
        second_traffic_violation = TrafficViolation(
            IdentityCard("35.595.089-3", "José de Queiroz"),
            LicensePlate("OXH-2070")
        )
        traffic_violations = [
            first_traffic_violation, second_traffic_violation
        ]

        output_string = OutputSerializer(traffic_violations).output_string()

        self.assertEqual(
            output_string, [
                "22.193.598-8; Ericka; QTB-0067",
                "35.595.089-3; José de Queiroz; OXH-2070"
            ]
        )
