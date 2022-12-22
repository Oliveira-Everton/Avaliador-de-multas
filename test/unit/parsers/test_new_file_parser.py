import unittest

from penalty_calculate.parsers.new_file_parser import NewFileParser


class TestNewFileParser(unittest.TestCase):

    def test_take_national_identity_cards(self):
        csv_file = NewFileParser("Transit Ticket input 1.csv")

        id_cards = csv_file.take_national_identity_cards()

        self.assertEqual(
            id_cards,
            None
        )
