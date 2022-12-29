import unittest

from penalty_calculate.serializers.output_serializer import OutputSerializer
from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.traffic_violation import TrafficViolation
from penalty_calculate.models.license_plate import LicensePlate


class TestOutputSerializer(unittest.TestCase):

    def test_output_string(self):
        first_id_card = IdentityCard("22.193.598-8", "Ericka")
        second_id_card = IdentityCard("35.595.089-3", "José de Queiroz")
        first_plate = LicensePlate("QTB-0067")
        second_plate = LicensePlate("OXH-2070")
        output_serializer = OutputSerializer(
            TrafficViolation(
                models_id_cards=[first_id_card, second_id_card],
                license_plates=[first_plate, second_plate]
            )
        )

        output_string = output_serializer.output_string()

        self.assertEqual(
            output_string,
            [
                "22.193.598-8; Ericka",
                "35.595.089-3; José de Queiroz",
                "QTB-0067", "OXH-2070"
            ]
        )
