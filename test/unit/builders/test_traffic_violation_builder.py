import unittest

from datetime import datetime

from main_penalty_calculate.builders import TrafficViolationBuilder
from main_penalty_calculate.constants import TypeInfractionStrings
from main_penalty_calculate.models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate
)


class TestTrafficViolationBuilder(unittest.TestCase):
    def test_build_traffic_violations_type_infraction_very_serious(self):
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
                    '1275-01-30 15:00:00',
                    '1275-02-01 10:00:00',
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
                    type_infraction=TypeInfractionStrings.VERY_SERIOUS,
                    infraction_date=datetime(1275, 1, 30, 15),
                    notification_date=datetime(1275, 2, 1, 10)
                )
            ]
        )

    def test_build_traffic_violations_type_infraction_serious(self):
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
                    'Grave',
                    '1275-01-30 15:00:00',
                    '1275-02-01 10:00:00',
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
                    type_infraction=TypeInfractionStrings.SERIOUS,
                    infraction_date=datetime(1275, 1, 30, 15),
                    notification_date=datetime(1275, 2, 1, 10)
                )
            ]
        )

    def test_build_traffic_violations_type_infraction_average(self):
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
                    'Média',
                    '1275-01-30 15:00:00',
                    '1275-02-01 10:00:00',
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
                    type_infraction=TypeInfractionStrings.AVERAGE,
                    infraction_date=datetime(1275, 1, 30, 15),
                    notification_date=datetime(1275, 2, 1, 10)
                )
            ]
        )

    def test_build_traffic_violations_type_infraction_light(self):
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
                    'Leve',
                    '1275-01-30 15:00:00',
                    '1275-02-01 10:00:00',
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
                    type_infraction=TypeInfractionStrings.LIGHT,
                    infraction_date=datetime(1275, 1, 30, 15),
                    notification_date=datetime(1275, 2, 1, 10)
                )
            ]
        )
