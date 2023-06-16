import unittest

from main_penalty_calculate.models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate
)


class TestTrafficViolation(unittest.TestCase):
    def test_identity_card_name(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694')
        )

        identity_card_name = traffic_violation.identity_card_name

        self.assertEqual(identity_card_name, 'Miho')

    def test_identity_card_number(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694')
        )

        identity_card_number = traffic_violation.identity_card_number

        self.assertEqual(identity_card_number, '13.386.966-0')

    def test_license_plate_number(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694')
        )

        license_plate_number = traffic_violation.license_plate_number

        self.assertEqual(license_plate_number, 'RXO-0694')
