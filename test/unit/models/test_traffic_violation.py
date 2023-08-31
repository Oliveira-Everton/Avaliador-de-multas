import unittest

from datetime import datetime

from main_penalty_calculate.models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate
)
from main_penalty_calculate.constants import TypeInfractionStrings


class TestTrafficViolation(unittest.TestCase):
    def test_traffic_violation_identity_card_name(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction=TypeInfractionStrings.LIGHT,
            infraction_date=datetime(1999, 1, 3, 12),
            notification_date=datetime(1999, 1, 4, 7)
        )

        identity_card_name = traffic_violation.identity_card.name

        self.assertEqual(identity_card_name, 'Miho')

    def test_traffic_violation_identity_card_number(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction=TypeInfractionStrings.LIGHT,
            infraction_date=datetime(1999, 1, 3, 12),
            notification_date=datetime(1999, 1, 4, 7)
        )

        identity_card_number = traffic_violation.identity_card.number

        self.assertEqual(identity_card_number, '13.386.966-0')

    def test_traffic_violation_license_plate_number(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction=TypeInfractionStrings.LIGHT,
            infraction_date=datetime(1999, 1, 3, 12),
            notification_date=datetime(1999, 1, 4, 7)
        )

        license_plate_number = traffic_violation.license_plate.number

        self.assertEqual(license_plate_number, 'RXO-0694')

    def test_traffic_violation_type_infraction(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction=TypeInfractionStrings.LIGHT,
            infraction_date=datetime(1999, 1, 3, 12),
            notification_date=datetime(1999, 1, 4, 7)
        )

        type_infraction = traffic_violation.type_infraction

        self.assertEqual(type_infraction, TypeInfractionStrings.LIGHT)

    def test_traffic_violation_infraction_date(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction=TypeInfractionStrings.LIGHT,
            infraction_date=datetime(1999, 1, 3, 12),
            notification_date=datetime(1999, 1, 4, 7)
        )

        infraction_date = traffic_violation.infraction_date

        self.assertEqual(
            infraction_date, datetime(1999, 1, 3, 12)
        )

    def test_traffic_violation_notification_date(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction=TypeInfractionStrings.LIGHT,
            infraction_date=datetime(1999, 1, 3, 12),
            notification_date=datetime(1999, 1, 4, 7)
        )

        notification_date = traffic_violation.notification_date

        self.assertEqual(
            notification_date, datetime(1999, 1, 4, 7)
        )

    def test_traffic_violation_identity_card(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction=TypeInfractionStrings.LIGHT,
            infraction_date=datetime(1999, 1, 3, 12),
            notification_date=datetime(1999, 1, 4, 7)
        )

        identity_card = traffic_violation.identity_card

        self.assertEqual(
            identity_card, IdentityCard('13.386.966-0', 'Miho')
        )

    def test_traffic_violation_license_plate(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction=TypeInfractionStrings.LIGHT,
            infraction_date=datetime(1999, 1, 3, 12),
            notification_date=datetime(1999, 1, 4, 7)
        )

        license_plate = traffic_violation.license_plate

        self.assertEqual(
            license_plate, LicensePlate('RXO-0694')
        )

    def test_traffic_violation_properties_values(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction=TypeInfractionStrings.LIGHT,
            infraction_date=datetime(1999, 1, 3, 12),
            notification_date=datetime(1999, 1, 4, 7)
        )

        properties_values = traffic_violation.properties_values()

        expected_infraction_date = datetime(1999, 1, 3, 12)
        expected_notification_date = datetime(1999, 1, 4, 7)
        expected_type_infraction = TypeInfractionStrings.LIGHT
        expected_properties_values = [
            IdentityCard('13.386.966-0', 'Miho'),
            LicensePlate('RXO-0694'),
            expected_type_infraction,
            expected_infraction_date,
            expected_notification_date
        ]
        self.assertEqual(properties_values, expected_properties_values)
