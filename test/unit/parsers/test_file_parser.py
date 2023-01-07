import unittest

from penalty_calculate.parsers.file_parser import FileParser


class TestFileParser(unittest.TestCase):

    def test_output_file(self):
        csv_parser = FileParser("Transit Ticket input 1.csv")

        traffic_violations = csv_parser.traffic_violations()

        self.assertEqual(
            len(traffic_violations), 6
        )
