import unittest

from main_penalty_calculate.parsers import FileParser
from main_penalty_calculate.models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate,
)


class TestFileParser(unittest.TestCase):
    def test_file_parser_build_traffic_violations(self):
        csv_parser = FileParser("Transit Ticket input 1.csv")

        traffic_violations = csv_parser.build_traffic_violations()

        self.assertEqual(
            traffic_violations, [
                TrafficViolation(
                    IdentityCard(
                        name="Josevaldo Cal. O. Teiro",
                        number="467191153"
                    ),
                    LicensePlate(
                        number='ARE-9420'
                    )
                ),
                TrafficViolation(
                    IdentityCard(
                        name="Josevaldo Cal. O. Teiro",
                        number="467191153"
                    ),
                    LicensePlate(
                        number='KVI-2310'
                    )
                ),
                TrafficViolation(
                    IdentityCard(
                        name="Josevaldo Cal. O. Teiro",
                        number="467191153"
                    ),
                    LicensePlate(
                        number='KVI-2310'
                    )
                ),
                TrafficViolation(
                    IdentityCard(
                        name="Josevaldo Cal. O. Teiro",
                        number="467191153"
                    ),
                    LicensePlate(
                        number='ARE-9420'
                    )
                ),
                TrafficViolation(
                    IdentityCard(
                        name="Osvaldo Plinio",
                        number="276787067"
                    ),
                    LicensePlate(
                        number='BIO-9626'
                    )
                ),
                TrafficViolation(
                    IdentityCard(
                        name="Gerusa Juventina",
                        number="149178360"
                    ),
                    LicensePlate(
                        number='SOS-3257'
                    )
                )
            ]
        )
