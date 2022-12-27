import unittest

from penalty_calculate.models.traffic_violation import TrafficViolation


class TestTrafficViolation(unittest.TestCase):
    def test_take_models_id(self):
        traffic_violation = TrafficViolation(
            models_id=["models"]
        )

        models_id = traffic_violation.id_cards

        self.assertEqual(models_id, ["models"])

    def test_take_models_plates(self):
        traffic_violation = TrafficViolation(
            license_plates=["models plates"]
        )

        models_plates = traffic_violation.license_plates

        self.assertEqual(models_plates, ["models plates"])
