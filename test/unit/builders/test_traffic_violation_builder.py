import unittest

from main_penalty_calculate.builders import TrafficViolationBuilder
from main_penalty_calculate.models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate
)


class TestTrafficViolationBuilder(unittest.TestCase):
    def test_build_traffic_violations(self):
        converted_file = [
            (
                0, [
                    'Placa',
                    'Tipo de infração',
                    'Data da infração',
                    'Data da notificação',
                    'Data de pagamento',
                    'RG do infrator',
                    'Nome do infrator',
                ]
            ),
            (
                1, [
                    'MGN-9130',
                    'Gravíssima',
                    '975-01-30 15:00:00',
                    '975-02-01 10:00:00',
                    '',
                    '138469945',
                    'Morgan'
                ]
            )
        ]

        traffic_violations = TrafficViolationBuilder(
            converted_file
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
