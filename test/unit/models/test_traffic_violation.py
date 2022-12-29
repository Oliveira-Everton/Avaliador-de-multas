import unittest

from penalty_calculate.models.traffic_violation import TrafficViolation


class TestTrafficViolation(unittest.TestCase):

    def test_property_models_id(self):
        traffic_violation = TrafficViolation(
            models_id_cards=["models"]
        )

        models_id_cards = traffic_violation.id_cards

        self.assertEqual(models_id_cards, ["models"])

    def test_property_models_plates(self):
        traffic_violation = TrafficViolation(
            license_plates=["models plates"]
        )

        models_plates = traffic_violation.license_plates

        self.assertEqual(models_plates, ["models plates"])
