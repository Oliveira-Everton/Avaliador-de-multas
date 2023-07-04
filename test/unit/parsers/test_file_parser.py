import unittest

from main_penalty_calculate.parsers import FileParser


class TestFileParser(unittest.TestCase):
    def test_convert_file(self):
        csv_parser = FileParser(
            'Transit Ticket input 2.csv'
        )

        pre_traffic_violation = csv_parser.pre_traffic_violations()

        self.assertEqual(
            pre_traffic_violation, [
                {
                    'identity_card_name': 'Dtcv. Olivera',
                    'identity_card_number': '375944035',
                    'license_plate_number': 'QBJ-6840',
                    'type_infraction': 'Gravíssima',
                    'infraction_date': '1890-01-01 12:00:00',
                    'notification_date': '1890-03-28 07:00:00'
                },
                {
                    'identity_card_name': 'Weihi Imawee',
                    'identity_card_number': '475936607',
                    'license_plate_number': 'NEK-6986',
                    'type_infraction': 'Média',
                    'infraction_date': '2030-05-19 16:00:00',
                    'notification_date': '2030-06-30 12:00:00'
                },
                {
                    'identity_card_name': 'Morgan Lyori',
                    'identity_card_number': '138469945',
                    'license_plate_number': 'MGN-9130',
                    'type_infraction': 'Leve',
                    'infraction_date': '1750-01-01 12:00:00',
                    'notification_date': '1750-05-04 07:00:00'
                }
            ]
        )
