import unittest

from penalty_calculate.parsers.file_parser import FileParser


class TestFileParser(unittest.TestCase):

    def test_traffic_violations(self):
        csv_parser = FileParser("Transit Ticket input 1.csv")

        traffic_violations = csv_parser.traffic_violations()

        self.assertEqual(
            type(traffic_violations), list
        )
