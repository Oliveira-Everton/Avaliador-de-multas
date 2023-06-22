import unittest

from main_penalty_calculate.builders import ViolatorsAvaliationsBuilder
from main_penalty_calculate.models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate,
    ViolatorAvaliation
)


class TestViolatorsAvaliationsBuilder(unittest.TestCase):
    def test_build_violator_avaliation(self):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('IDE-3516'),
                type_infraction='Grave',
                infraction_date='1999-10-01 06:12:22',
                notification_date='1999-11-04 08:00:00'
            ),
            TrafficViolation(
                identity_card=IdentityCard('13.386.966-0', 'Miho'),
                license_plate=LicensePlate('RXO-0694'),
                type_infraction='Leve',
                infraction_date='2000-01-03 12:00:00',
                notification_date='2000-01-04 07:27:42'
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
                    demerit_points=0
                ),
                ViolatorAvaliation(
                    identity_card=IdentityCard('13.386.966-0', 'Miho'),
                    license_plates=['RXO-0694'],
                    demerit_points=3
                )
            ]
        )

    def test_build_violator_avaliation_with_more_plates_in_identity_card(self):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('IDE-3516'),
                type_infraction='Grave',
                infraction_date='1999-10-01 06:12:22',
                notification_date='1999-11-04 08:00:00'
            ),
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('NAQ-5775'),
                type_infraction='Leve',
                infraction_date='1999-10-11 06:12:22',
                notification_date='1999-10-16 08:00:00'
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
                    demerit_points=3
                )
            ]
        )

    def test_build_violator_avaliation_with_repeated_plates(self):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('IDE-3516'),
                type_infraction='Leve',
                infraction_date='1999-10-01 06:12:22',
                notification_date='1999-11-04 08:00:00'
            ),
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('NAQ-5775'),
                type_infraction='Grave',
                infraction_date='1999-10-01 06:12:22',
                notification_date='1999-11-04 08:00:00'
            ),
            TrafficViolation(
                identity_card=IdentityCard('13.386.966-0', 'Miho'),
                license_plate=LicensePlate('RXO-0694'),
                type_infraction='Leve',
                infraction_date='2000-01-01 12:00:00',
                notification_date='2000-01-05 07:27:42'
            ),
            TrafficViolation(
                identity_card=IdentityCard('13.386.966-0', 'Miho'),
                license_plate=LicensePlate('RXO-0694'),
                type_infraction='Leve',
                infraction_date='2000-06-11 12:00:00',
                notification_date='2000-06-12 07:27:42'
            ),
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('IDE-3516'),
                type_infraction='Grave',
                infraction_date='2000-02-02 12:00:00',
                notification_date='2000-02-03 07:27:42'
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
                    license_plates=['IDE-3516', 'NAQ-5775'],
                    demerit_points=5
                ),
                ViolatorAvaliation(
                    identity_card=IdentityCard('13.386.966-0', 'Miho'),
                    license_plates=['RXO-0694'],
                    demerit_points=6
                )
            ]
        )

    def test_build_violator_avaliation_demerit_points(self):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('13.846.994-5', 'Morgan'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction='Gravíssima',
                infraction_date='1750-01-01 12:00:00',
                notification_date='1750-01-04 07:00:00'
            ),
            TrafficViolation(
                identity_card=IdentityCard('37.594.403-5', 'Det. Olivera'),
                license_plate=LicensePlate('QBJ-6840'),
                type_infraction='Média',
                infraction_date='1890-01-01 12:00:00',
                notification_date='1890-01-02 07:00:00'
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
                ),
                ViolatorAvaliation(
                    identity_card=IdentityCard('37.594.403-5', 'Det. Olivera'),
                    license_plates=['QBJ-6840'],
                    demerit_points=4
                )
            ]
        )

    def test_build_violator_avaliation_invalid_demerit_points(self):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('13.846.994-5', 'Morgan'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction='Gravíssima',
                infraction_date='1750-01-01 12:00:00',
                notification_date='1750-05-04 07:00:00'
            ),
            TrafficViolation(
                identity_card=IdentityCard('37.594.403-5', 'Det. Olivera'),
                license_plate=LicensePlate('QBJ-6840'),
                type_infraction='Média',
                infraction_date='1890-01-01 12:00:00',
                notification_date='1890-03-28 07:00:00'
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
                ),
                ViolatorAvaliation(
                    identity_card=IdentityCard('37.594.403-5', 'Det. Olivera'),
                    license_plates=['QBJ-6840'],
                    demerit_points=0
                )
            ]
        )

    def test_build_violator_avaliation_sum_demerit_points(self):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('37.594.403-5', 'Det. Olivera'),
                license_plate=LicensePlate('QBJ-6840'),
                type_infraction='Média',
                infraction_date='1890-01-01 12:00:00',
                notification_date='1890-01-03 07:00:00'
            ),
            TrafficViolation(
                identity_card=IdentityCard('37.594.403-5', 'Det. Olivera'),
                license_plate=LicensePlate('QBJ-6840'),
                type_infraction='Média',
                infraction_date='1890-09-03 12:00:00',
                notification_date='1890-09-06 07:00:00'
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
