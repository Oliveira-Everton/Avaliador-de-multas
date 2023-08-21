import unittest

from datetime import datetime

from main_penalty_calculate.models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate
)
from main_penalty_calculate.constants import TypeInfractionStrings


class TestTrafficViolation(unittest.TestCase):
    def test_identity_card_name(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction=TypeInfractionStrings.LIGHT,
            infraction_date=datetime(1999, 1, 3, 12),
            notification_date=datetime(1999, 1, 4, 7)
        )

        identity_card_name = traffic_violation.identity_card_name

        self.assertEqual(identity_card_name, 'Miho')

    def test_identity_card_number(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction=TypeInfractionStrings.LIGHT,
            infraction_date=datetime(1999, 1, 3, 12),
            notification_date=datetime(1999, 1, 4, 7)
        )

        identity_card_number = traffic_violation.identity_card_number

        self.assertEqual(identity_card_number, '13.386.966-0')

    def test_license_plate_number(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction=TypeInfractionStrings.LIGHT,
            infraction_date=datetime(1999, 1, 3, 12),
            notification_date=datetime(1999, 1, 4, 7)
        )

        license_plate_number = traffic_violation.license_plate_number

        self.assertEqual(license_plate_number, 'RXO-0694')

    def test_type_infraction(self):
        traffic_violation = TrafficViolation(
            identity_card=IdentityCard('13.386.966-0', 'Miho'),
            license_plate=LicensePlate('RXO-0694'),
            type_infraction=TypeInfractionStrings.LIGHT,
            infraction_date=datetime(1999, 1, 3, 12),
            notification_date=datetime(1999, 1, 4, 7)
        )

        type_infraction = traffic_violation.type_infraction

        self.assertEqual(type_infraction, TypeInfractionStrings.LIGHT)

    def test_infraction_date(self):
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

    def test_notification_date(self):
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

    def test_identity_card(self):
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
