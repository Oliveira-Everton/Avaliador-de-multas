import unittest

from penalty_calculate.models.identity_card import IdentityCard


class TestIdentityCard(unittest.TestCase):
    def test_property_identity_name(self):
        identity_card = IdentityCard("37.594.403-5", "Dtcv. Olivera")

        identity_name = identity_card.name

        self.assertEqual(identity_name, "Dtcv. Olivera")

    def test_property_identity_number(self):
        identity_card = IdentityCard("37.594.403-5", "Dtcv. Olivera")

        identity_number = identity_card.number

        self.assertEqual(identity_number, "37.594.403-5")
