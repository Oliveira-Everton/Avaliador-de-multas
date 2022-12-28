import unittest

from penalty_calculate.parsers.file_parser import FileParser


class TestFileParser(unittest.TestCase):

    def test_output_file(self):
        csv_parser = FileParser("Transit Ticket input 1.csv")

        output_file = csv_parser.output_file()

        self.assertEqual(
            output_file, [
                '467191153; Josevaldo Cal. O. Teiro',
                '467191153; Josevaldo Cal. O. Teiro',
                '467191153; Josevaldo Cal. O. Teiro',
                '467191153; Josevaldo Cal. O. Teiro',
                '276787067; Osvaldo Plinio',
                '149178360; Gerusa Juventina',
                'ARE-9420', 'KVI-2310', 'KVI-2310',
                'ARE-9420', 'BIO-9626', 'SOS-3257'
            ]
        )
