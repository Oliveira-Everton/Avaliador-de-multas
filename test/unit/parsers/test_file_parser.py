import unittest

from main_penalty_calculate.parsers import FileParser


class TestFileParser(unittest.TestCase):
    def test_convert_file(self):
        csv_parser = FileParser(
            'Transit Ticket input 1.csv'
        )

        converted_file = csv_parser.convert_file()

        self.assertEqual(
            converted_file, [
                (
                    0, [
                        'Placa',
                        'Tipo de infração',
                        'Data da infração',
                        'Data da notificação',
                        'Data de pagamento',
                        'RG do infrator',
                        'Nome do infrator'
                    ]
                ),
                (
                    1, [
                        'ARE-9420',
                        'Gravíssima',
                        '1999-11-05 15:00:00',
                        '2000-01-25 10:00:00',
                        '',
                        '467191153',
                        'Josevaldo Cal. O. Teiro'
                    ]
                ),
                (
                    2, [
                        'KVI-2310',
                        'Gravíssima',
                        '2000-01-01 15:00:00',
                        '2000-01-04 10:00:00',
                        '',
                        '467191153',
                        'Josevaldo Cal. O. Teiro'
                    ]
                ),
                (
                    3, [
                        'KVI-2310',
                        'Grave',
                        '2000-01-04 15:00:00',
                        '2000-01-05 10:00:00',
                        '',
                        '467191153',
                        'Josevaldo Cal. O. Teiro'
                    ]
                ),
                (
                    4, [
                        'ARE-9420',
                        'Gravíssima',
                        '2000-01-10 15:00:00',
                        '2000-01-25 10:00:00',
                        '',
                        '467191153',
                        'Josevaldo Cal. O. Teiro'
                    ]
                ),
                (
                    5, [
                        'BIO-9626',
                        'Grave',
                        '2000-02-05 14:00:00',
                        '2000-02-10 11:00:00',
                        '',
                        '276787067',
                        'Osvaldo Plinio'
                    ]
                ),
                (
                    6, [
                        'SOS-3257',
                        'Média',
                        '2000-08-16 16:00:00',
                        '2000-02-11 12:00:00',
                        '',
                        '149178360',
                        'Gerusa Juventina'
                    ]
                )
            ]
        )
