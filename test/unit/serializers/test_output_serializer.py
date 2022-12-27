import unittest

from penalty_calculate.serializers.output_serializer import OutputSerializer
from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.traffic_violation import TrafficViolation
from penalty_calculate.models.license_plate import LicensePlate


class TestOutputSerializer(unittest.TestCase):
    def test_take_models_id(self):
        first_id_card = IdentityCard("22.193.598-8", "Ericka")
        second_id_card = IdentityCard("35.595.089-3", "José de Queiroz")
        output_serializer = OutputSerializer(
            TrafficViolation(
                models_id=[first_id_card, second_id_card]
            )
        )

        output_id = output_serializer.output_id()

        self.assertEqual(
            output_id, [('22.193.598-8', 'Ericka'), ('35.595.089-3', 'José de Queiroz')]
        )

    def test_take_models_plates(self):
        first_plate = LicensePlate("QTB-0067")
        second_plate = LicensePlate("OXH-2070")
        output_serializer = OutputSerializer(
            TrafficViolation(
                license_plates=[first_plate, second_plate]
            )
        )

        output_plate = output_serializer.output_plate()

        self.assertEqual(
            output_plate, ['QTB-0067', 'OXH-2070']
        )

    def test_output_string(self):
        se_id_card = IdentityCard("35.595.089-8", "Jos")
        first_id_card = IdentityCard("22.193.598-8", "Ericka")
        second_id_card = IdentityCard("35.595.089-3", "José de Queiroz")
        first_plate = LicensePlate("QTB-0067")
        second_plate = LicensePlate("OXH-2070")
        output_serializer = OutputSerializer(
            TrafficViolation(
                models_id=[se_id_card, first_id_card, second_id_card],
                license_plates=[first_plate, second_plate]
            )
        )

        output_string = output_serializer.output_string()

        self.assertEqual(
            output_string, None
        )