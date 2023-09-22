import unittest

from datetime import datetime

from main_penalty_calculate.builders import ViolatorsAvaliationsBuilder
from main_penalty_calculate.models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate,
    ViolatorAvaliation
)
from main_penalty_calculate.constants import TypeInfractionStrings


class TestViolatorsAvaliationsBuilder(unittest.TestCase):
    def test_build_violator_avaliation_with_different_identity_cards(self):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('IDE-3516'),
                type_infraction=TypeInfractionStrings.VERY_SERIOUS,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            ),
            TrafficViolation(
                identity_card=IdentityCard('13.386.966-0', 'Miho'),
                license_plate=LicensePlate('RXO-0694'),
                type_infraction=TypeInfractionStrings.LIGHT,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            )
        ]
        violators_avaliations_builder = ViolatorsAvaliationsBuilder(
            traffic_violations
        )

        violators_avaliations = (
            violators_avaliations_builder.build_violators_avaliations()
        )

        self.assertEqual(
            violators_avaliations, [
                ViolatorAvaliation(
                    identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                    license_plates=[LicensePlate('IDE-3516')],
                    demerit_points=7,
                    penalty_amount=293.47
                ),
                ViolatorAvaliation(
                    identity_card=IdentityCard('13.386.966-0', 'Miho'),
                    license_plates=[LicensePlate('RXO-0694')],
                    demerit_points=3,
                    penalty_amount=88.38
                )
            ]
        )

    def test_build_violator_avaliation_with_repeated_identity_card(self):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('IDE-3516'),
                type_infraction=TypeInfractionStrings.SERIOUS,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            ),
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('NAQ-5775'),
                type_infraction=TypeInfractionStrings.LIGHT,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            ),
        ]
        violators_avaliations_builder = ViolatorsAvaliationsBuilder(
            traffic_violations
        )

        violators_avaliations = (
            violators_avaliations_builder.build_violators_avaliations()
        )

        self.assertEqual(
            violators_avaliations, [
                ViolatorAvaliation(
                    identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                    license_plates=[
                        LicensePlate('IDE-3516'),
                        LicensePlate('NAQ-5775')
                    ],
                    demerit_points=8,
                    penalty_amount=283.61
                )
            ]
        )

    def test_build_violator_avaliation_with_repeated_license_plates(self):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('37.594.403-5', 'Det. Olivera'),
                license_plate=LicensePlate('QBJ-6840'),
                type_infraction=TypeInfractionStrings.AVERAGE,
                infraction_date=datetime(1999, 1, 1, 12),
                notification_date=datetime(1999, 1, 3, 7)
            ),
            TrafficViolation(
                identity_card=IdentityCard('37.594.403-5', 'Det. Olivera'),
                license_plate=LicensePlate('QBJ-6840'),
                type_infraction=TypeInfractionStrings.AVERAGE,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 6, 7)
            )
        ]
        violators_avaliations_builder = ViolatorsAvaliationsBuilder(
            traffic_violations
        )

        violators_avaliations = (
            violators_avaliations_builder.build_violators_avaliations()
        )

        self.assertEqual(
            violators_avaliations, [
                ViolatorAvaliation(
                    identity_card=IdentityCard('37.594.403-5', 'Det. Olivera'),
                    license_plates=[LicensePlate('QBJ-6840')],
                    demerit_points=8,
                    penalty_amount=260.32
                )
            ]
        )
