import unittest

from penalty_calculate.models.traffic_violation import TrafficViolation
from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.license_plate import LicensePlate


class TestTrafficViolation(unittest.TestCase):
    def test_property_name(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard("13.386.966-0", "Miho"),
            license_plate=LicensePlate('RXO-0694')
        )

        identity_card_name = traffic_violation.identity_card_name

        self.assertEqual(identity_card_name, 'Miho')

    def test_property_number(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard("13.386.966-0", "Miho"),
            license_plate=LicensePlate('RXO-0694')
        )

        identity_card_number = traffic_violation.identity_card_number

        self.assertEqual(identity_card_number, '13.386.966-0')

    def test_property_model_plate(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard("13.386.966-0", "Miho"),
            license_plate=LicensePlate('RXO-0694')
        )

        license_plate = traffic_violation.license_plate_number

        self.assertEqual(license_plate, 'RXO-0694')
