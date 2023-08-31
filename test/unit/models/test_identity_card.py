import unittest

from main_penalty_calculate.models import IdentityCard


class TestIdentityCard(unittest.TestCase):
    def test_identity_card_name(self):
        identity_card = IdentityCard('37.594.403-5', 'Dtcv. Olivera')

        identity_name = identity_card.name

        self.assertEqual(identity_name, 'Dtcv. Olivera')

    def test_identity_card_number(self):
        identity_card = IdentityCard('37.594.403-5', 'Dtcv. Olivera')

        identity_number = identity_card.number

        self.assertEqual(identity_number, '37.594.403-5')

    def test_identity_card_properties_values(self):
        identity_card = IdentityCard('37.594.403-5', 'Dtcv. Olivera')

        properties_values = identity_card.properties_values()

        self.assertEqual(
            properties_values, ['37.594.403-5', 'Dtcv. Olivera']
        )
