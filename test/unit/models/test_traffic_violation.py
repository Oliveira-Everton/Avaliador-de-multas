import unittest

from penalty_calculate.models.traffic_violation import TrafficViolation
from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.license_plate import LicensePlate


class TestTrafficViolation(unittest.TestCase):

    def test_property_model_id(self):
        traffic_violation = TrafficViolation(
            model_id_card=IdentityCard("13.386.966-0", "Miho")
        )

        id_card_name = traffic_violation.id_card.name
        id_card_number = traffic_violation.id_card.number

        self.assertEqual(id_card_name, 'Miho')
        self.assertEqual(id_card_number, '13.386.966-0')

    def test_property_model_plate(self):
        traffic_violation = TrafficViolation(
            model_license_plate=LicensePlate('RXO-0694')
        )

        license_plate = traffic_violation.license_plate.number

        self.assertEqual(license_plate, 'RXO-0694')
