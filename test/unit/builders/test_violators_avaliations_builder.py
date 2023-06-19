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
                type_infraction='grave'
            ),
            TrafficViolation(
                identity_card=IdentityCard('13.386.966-0', 'Miho'),
                license_plate=LicensePlate('RXO-0694'),
                type_infraction='leve'
            )
        ]
        violator_avaliation_builder = ViolatorsAvaliationsBuilder(
            traffic_violations
        )

        violators_avaliations = (
            violator_avaliation_builder.build_violators_avaliations()
        )

        self.assertEqual(
            violators_avaliations, [
                ViolatorAvaliation(
                    identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                    license_plates=['IDE-3516']
                ),
                ViolatorAvaliation(
                    identity_card=IdentityCard('13.386.966-0', 'Miho'),
                    license_plates=['RXO-0694']
                )
            ]
        )

    def test_build_violator_avaliation_with_more_plates_in_identity_card(self):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('IDE-3516'),
                type_infraction='grave'
            ),
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('NAQ-5775'),
                type_infraction='leve'
            ),
        ]
        violator_avaliation_builder = ViolatorsAvaliationsBuilder(
            traffic_violations
        )

        violators_avaliations = (
            violator_avaliation_builder.build_violators_avaliations()
        )

        self.assertEqual(
            violators_avaliations, [
                ViolatorAvaliation(
                    identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                    license_plates=['IDE-3516', 'NAQ-5775']
                )
            ]
        )

    def test_build_violator_avaliation_with_repeated_plates(self):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('IDE-3516'),
                type_infraction='leve'
            ),
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('NAQ-5775'),
                type_infraction='grave'
            ),
            TrafficViolation(
                identity_card=IdentityCard('13.386.966-0', 'Miho'),
                license_plate=LicensePlate('RXO-0694'),
                type_infraction='leve'
            ),
            TrafficViolation(
                identity_card=IdentityCard('13.386.966-0', 'Miho'),
                license_plate=LicensePlate('RXO-0694'),
                type_infraction='leve'
            ),
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('IDE-3516'),
                type_infraction='grave'
            )
        ]
        violator_avaliation_builder = ViolatorsAvaliationsBuilder(
            traffic_violations
        )

        violators_avaliations = (
            violator_avaliation_builder.build_violators_avaliations()
        )

        self.assertEqual(
            violators_avaliations, [
                ViolatorAvaliation(
                    identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                    license_plates=['IDE-3516', 'NAQ-5775']
                ),
                ViolatorAvaliation(
                    identity_card=IdentityCard('13.386.966-0', 'Miho'),
                    license_plates=['RXO-0694']
                )
            ]
        )
