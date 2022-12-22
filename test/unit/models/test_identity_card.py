import unittest

from penalty_calculate.models.identity_card import IdentityCard


class TestIdentityCard(unittest.TestCase):
    def test_return_id_name(self):
        id_card = IdentityCard("37.594.403-5", "Dtcv. Olivera")

        id_name = id_card.name

        self.assertEqual(id_name, "Dtcv. Olivera")

    def test_return_id_number(self):
        id_card = IdentityCard("37.594.403-5", "Dtcv. Olivera")

        id_number = id_card.number

        self.assertEqual(id_number, "37.594.403-5")
