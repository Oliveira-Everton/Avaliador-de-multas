import unittest

from main_penalty_calculate.builders import ViolatorsAvaliationsBuilder
from main_penalty_calculate.models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate,
    LicensePlates,
    ViolatorAvaliation
)


class TestViolatorsAvaliationsBuilder(unittest.TestCase):
    def test_violations_manager_build_violator_avaliation(self):
        traffic_violations = [
            TrafficViolation(
                identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                license_plate=LicensePlate('IDE-3516'),
                type_infraction='Gravíssima',
                infraction_date='1999-10-01 06:12:22',
                notification_date='1999-11-04 08:00:00',
                pay_date='1999-11-04 08:00:00'
            ),
            TrafficViolation(
                identity_card=IdentityCard('13.386.966-0', 'Miho'),
                license_plate=LicensePlate('RXO-0694'),
                type_infraction='Média',
                infraction_date='2000-01-01 12:00:00',
                notification_date='2000-01-05 07:27:42',
                pay_date=''
            )
        ]
        violators_avaliations = ViolatorsAvaliationsBuilder(traffic_violations)

        violator_avaliation = (
            violators_avaliations.build_violators_avaliations()
        )

        self.assertEqual(
            violator_avaliation, [
                ViolatorAvaliation(
                    identity_card=IdentityCard('19.632.142-6', 'Takashi'),
                    license_plates=LicensePlates([['IDE-3516']])
                ),
                ViolatorAvaliation(
                    identity_card=IdentityCard('13.386.966-0', 'Miho'),
                    license_plates=LicensePlates([['RXO-0694']])
                )
            ]
        )
