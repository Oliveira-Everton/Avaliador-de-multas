import unittest

from penalty_calculate.managers.id_cards_manager import IdCardsManager
from penalty_calculate.models.identity_cards import IdentityCards


class TestIdCardsManager(unittest.TestCase):
    def test_take_id_cards(self):
        id_cards = IdCardsManager(
            IdentityCards(
                identity_numbers=["19.466.923-3", "19.304.130-3"],
                identity_names=["José de Queiroz", "Idle Zeller"]
            )
        )

        take_id_cards = id_cards.take_id_cards()

        self.assertEqual(
            take_id_cards,
            [
                {"19.466.923-3": "José de Queiroz"},
                {"19.304.130-3": "Idle Zeller"}
            ]
        )

    def test_check_names(self):
        list_names = ["Hideki Hyuuga", "Morgan", "Ericka"]
        identity_cards = IdentityCards(identity_names=list_names)

        check_names = identity_cards.check_names()

        self.assertEqual(
            check_names, ["Hideki Hyuuga", "Morgan", "Ericka"]
        )
