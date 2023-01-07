import unittest

from penalty_calculate.serializers.output_serializer import OutputSerializer
from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.traffic_violation import TrafficViolation
from penalty_calculate.models.license_plate import LicensePlate


class TestOutputSerializer(unittest.TestCase):

    def test_output_string(self):
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
