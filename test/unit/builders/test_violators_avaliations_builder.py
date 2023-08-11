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
                    license_plates=['IDE-3516'],
                    demerit_points=7
                ),
                ViolatorAvaliation(
                    identity_card=IdentityCard('13.386.966-0', 'Miho'),
                    license_plates=['RXO-0694'],
                    demerit_points=3
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
                    license_plates=['IDE-3516', 'NAQ-5775'],
                    demerit_points=8
                )
            ]
        )

    def test_build_violator_avaliation_all_type_infractions(self):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('13.846.994-5', 'Morgan'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.LIGHT,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            ),
            TrafficViolation(
                identity_card=IdentityCard('37.594.403-5', 'Det. Olivera'),
                license_plate=LicensePlate('QBJ-6840'),
                type_infraction=TypeInfractionStrings.AVERAGE,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            ),
            TrafficViolation(
                identity_card=IdentityCard('13.386.966-0', 'Miho'),
                license_plate=LicensePlate('RXO-0694'),
                type_infraction=TypeInfractionStrings.SERIOUS,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            ),
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('IDE-3516'),
                type_infraction=TypeInfractionStrings.VERY_SERIOUS,
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
                    identity_card=IdentityCard('13.846.994-5', 'Morgan'),
                    license_plates=['MGN-9130'],
                    demerit_points=3
                ),
                ViolatorAvaliation(
                    identity_card=IdentityCard('37.594.403-5', 'Det. Olivera'),
                    license_plates=['QBJ-6840'],
                    demerit_points=4
                ),
                ViolatorAvaliation(
                    identity_card=IdentityCard('13.386.966-0', 'Miho'),
                    license_plates=['RXO-0694'],
                    demerit_points=5
                ),
                ViolatorAvaliation(
                    identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                    license_plates=['IDE-3516'],
                    demerit_points=7
                )
            ]
        )

    def test_build_violator_avaliation_demerit_points_29th_infrigement_period(
        self
    ):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('13.846.994-5', 'Morgan'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.VERY_SERIOUS,
                infraction_date=datetime(1999, 1, 1, 12),
                notification_date=datetime(1999, 1, 31, 7)
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
                    identity_card=IdentityCard('13.846.994-5', 'Morgan'),
                    license_plates=['MGN-9130'],
                    demerit_points=7
                )
            ]
        )

    def test_build_violator_avaliation_demerit_points_30th_infrigement_period(
        self
    ):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('13.846.994-5', 'Morgan'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.VERY_SERIOUS,
                infraction_date=datetime(1999, 1, 1, 12),
                notification_date=datetime(1999, 2, 1, 7)
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
                    identity_card=IdentityCard('13.846.994-5', 'Morgan'),
                    license_plates=['MGN-9130'],
                    demerit_points=7
                )
            ]
        )

    def test_build_violator_avaliation_demerit_points_31th_infrigement_period(
        self
    ):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('13.846.994-5', 'Morgan'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.VERY_SERIOUS,
                infraction_date=datetime(1999, 1, 1, 12),
                notification_date=datetime(1999, 2, 2, 7)
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
                    identity_card=IdentityCard('13.846.994-5', 'Morgan'),
                    license_plates=['MGN-9130'],
                    demerit_points=0
                )
            ]
        )

    def test_build_violator_avaliation_aggregate_demerit_points(self):
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
                    license_plates=['QBJ-6840'],
                    demerit_points=8
                )
            ]
        )
