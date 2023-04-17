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
            identity_card=IdentityCard("22.193.598-8", "Ericka"),
            license_plate=LicensePlate("QTB-0067"),
            type_infraction="Leve",
            infraction_date="2050-09-01 09:43:12"
        )
        second_traffic_violation = TrafficViolation(
            identity_card=IdentityCard("35.595.089-3", "José de Queiroz"),
            license_plate=LicensePlate("OXH-2070"),
            type_infraction="Grave",
            infraction_date="2022-10-02 20:27:44"
        )
        traffic_violations = [
            first_traffic_violation, second_traffic_violation
        ]

        output_string = OutputSerializer(traffic_violations).output_string()

        self.assertEqual(
            output_string, [
                "22.193.598-8; Ericka; QTB-0067; Leve; 2050-09-01 09:43:12",
                "35.595.089-3; José de Queiroz; OXH-2070; Grave; 2022-10-02 20:27:44"
            ]
        )
