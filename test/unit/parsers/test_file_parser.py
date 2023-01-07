import unittest

from penalty_calculate.parsers.file_parser import FileParser


class TestFileParser(unittest.TestCase):

    def test_output_file(self):
        csv_parser = FileParser("Transit Ticket input 1.csv")

        output_file = csv_parser.output_file()

        self.assertEqual(
            output_file, [
                '467191153; Josevaldo Cal. O. Teiro; ARE-9420',
                '467191153; Josevaldo Cal. O. Teiro; KVI-2310',
                '467191153; Josevaldo Cal. O. Teiro; KVI-2310',
                '467191153; Josevaldo Cal. O. Teiro; ARE-9420',
                '276787067; Osvaldo Plinio; BIO-9626',
                '149178360; Gerusa Juventina; SOS-3257'
            ]
        )
