import unittest

from penalty_calculate.models.identity_cards import IdentityCards


class TestIdentityCards(unittest.TestCase):
    def test_check_names(self):
        list_names = ["Hideki Hyuuga", "Morgan", "Ericka"]
        identity_cards = IdentityCards(identity_names=list_names)

        check_names = identity_cards.check_names()

        self.assertEqual(
            check_names, ["Hideki Hyuuga", "Morgan", "Ericka"]
        )

    def test_check_numbers(self):
        list_numbers = ["4002_8922", "666_666", "132022"]
        identity_cards = IdentityCards(identity_numbers=list_numbers)

        check_numbers = identity_cards.check_numbers()

        self.assertEqual(
            check_numbers, ["4002_8922", "666_666", "132022"]
        )

    def test_add_names(self):
        name = "Hideki"
        list_names = ["Morgan", "Ericka"]
        identity_cards = IdentityCards(
            identity_names=list_names
        )

        identity_cards.add_name(name)

        self.assertEqual(
            identity_cards.check_names(),
            ["Morgan", "Ericka", "Hideki"]
        )

    def test_add_numbers(self):
        number = "4002-8922"
        list_numbers = ["666", "13"]
        identity_cards = IdentityCards(
            identity_numbers=list_numbers
        )

        identity_cards.add_number(number)

        self.assertEqual(
            identity_cards.check_numbers(),
            ["666", "13", "4002-8922"]
        )
