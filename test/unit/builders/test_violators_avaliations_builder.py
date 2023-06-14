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
                license_plate=LicensePlate('IDE-3516')
            ),
            TrafficViolation(
                identity_card=IdentityCard('13.386.966-0', 'Miho'),
                license_plate=LicensePlate('RXO-0694')
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
