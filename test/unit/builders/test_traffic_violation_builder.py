import unittest

from main_penalty_calculate.builders import TrafficViolationBuilder
from main_penalty_calculate.models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate
)


class TestTrafficViolationBuilder(unittest.TestCase):
    def test_build_traffic_violations(self):
        pre_traffic_violations = [
            {
                'identity_card_name': 'Morgan',
                'identity_card_number': '138469945',
                'license_plate_number': 'MGN-9130',
                'type_infraction': 'Gravíssima',
                'infraction_date': '975-01-30 15:00:00',
                'notification_date': '975-02-01 10:00:00'
            }
        ]

        traffic_violations = TrafficViolationBuilder(
            pre_traffic_violations
        ).build_traffic_violations()

        self.assertEqual(
            traffic_violations, [
                TrafficViolation(
                    identity_card=IdentityCard(
                        name='Morgan',
                        number='138469945'
                    ),
                    license_plate=LicensePlate(
                        number='MGN-9130'
                    ),
                    type_infraction='Gravíssima',
                    infraction_date='975-01-30 15:00:00',
                    notification_date='975-02-01 10:00:00'
                )
            ]
        )
