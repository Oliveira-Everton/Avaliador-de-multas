import unittest

from penalty_calculate.managers.violations_manager import ViolationsManager
from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.traffic_violation import TrafficViolation
from penalty_calculate.models.license_plate import LicensePlate


class TestViolationsManager(unittest.TestCase):

    def test_property_violations_manager(self):
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

        violations = ViolationsManager(traffic_violations).traffic_violations

        self.assertEqual(
            violations, [
                first_traffic_violation,
                second_traffic_violation
            ]
        )
