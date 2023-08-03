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

    def test_build_traffic_violations_with_several_traffic_violations(self):
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
                    '1275-01-29 15:00:00',
                    '1275-01-30 10:00:00',
                    '',
                    '138469945',
                    'Morgan'
                ]
            ),
            (
                2, [
                    'QBJ-6840',
                    'Média',
                    '1890-01-01 12:00:00',
                    '1890-01-28 07:00:00',
                    '',
                    '375944035',
                    'Dtcv. Olivera'
                ]
            ),
            (
                3, [
                    'MVC-4848',
                    'Grave',
                    '1990-01-01 12:00:00',
                    '1990-01-06 07:00:00',
                    '',
                    '302864155',
                    'Vonkuzi Amelnay'
                ]
            ),
            (
                4, [
                    'RXO-0694',
                    'Gravíssima',
                    '1990-01-01 12:00:00',
                    '1990-01-06 07:00:00',
                    '',
                    '133869660',
                    'Miho'
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
                    infraction_date=datetime(1275, 1, 29, 15),
                    notification_date=datetime(1275, 1, 30, 10)
                ),
                TrafficViolation(
                    identity_card=IdentityCard(
                        name='Dtcv. Olivera',
                        number='375944035'
                    ),
                    license_plate=LicensePlate(
                        number='QBJ-6840'
                    ),
                    type_infraction=TypeInfractionStrings.AVERAGE,
                    infraction_date=datetime(1890, 1, 1, 12),
                    notification_date=datetime(1890, 1, 28, 7)
                ),
                TrafficViolation(
                    identity_card=IdentityCard(
                        name='Vonkuzi Amelnay',
                        number='302864155'
                    ),
                    license_plate=LicensePlate(
                        number='MVC-4848'
                    ),
                    type_infraction=TypeInfractionStrings.SERIOUS,
                    infraction_date=datetime(1990, 1, 1, 12),
                    notification_date=datetime(1990, 1, 6, 7)
                ),
                TrafficViolation(
                    identity_card=IdentityCard(
                        name='Miho',
                        number='133869660'
                    ),
                    license_plate=LicensePlate(
                        number='RXO-0694'
                    ),
                    type_infraction=TypeInfractionStrings.VERY_SERIOUS,
                    infraction_date=datetime(1990, 1, 1, 12),
                    notification_date=datetime(1990, 1, 6, 7)
                )
            ]
        )
