import unittest

from main_penalty_calculate.models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate
)


class TestTrafficViolation(unittest.TestCase):
    def test_traffic_violation_identity_card_name(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard("13.386.966-0", "Miho"),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction="Média",
            infraction_date="1865-10-06"
        )

        identity_card_name = traffic_violation.identity_card_name

        self.assertEqual(identity_card_name, 'Miho')

    def test_traffic_violation_identity_card_number(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard("13.386.966-0", "Miho"),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction="Média",
            infraction_date="1865-10-06"
        )

        identity_card_number = traffic_violation.identity_card_number

        self.assertEqual(identity_card_number, '13.386.966-0')

    def test_traffic_violation_license_plate_number(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard("13.386.966-0", "Miho"),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction="Média",
            infraction_date="1865-10-06 12:00:00"
        )

        license_plate_number = traffic_violation.license_plate_number

        self.assertEqual(license_plate_number, 'RXO-0694')

    def test_traffic_violation_type_infraction(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard("13.386.966-0", "Miho"),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction="Média",
            infraction_date="1865-10-06 12:00:00"
        )

        type_infraction = traffic_violation.type_infraction

        self.assertEqual(type_infraction, 'Média')

    def test_traffic_violation_infraction_date(self):
        traffic_violation = TrafficViolation(
            IdentityCard("20.478.823-7", "Takashi"),
            LicensePlate("MWR-5226"),
            type_infraction="Grave",
            infraction_date="1864-16-02 11:30:00"
        )

        infraction_date = traffic_violation.infraction_date

        self.assertEqual(infraction_date, "1864-16-02 11:30:00")
