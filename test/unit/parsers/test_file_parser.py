import unittest

from penalty_calculate.parsers.file_parser import FileParser
from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.license_plate import LicensePlate
from penalty_calculate.models.traffic_violation import TrafficViolation


class TestFileParser(unittest.TestCase):

    def test_traffic_violations(self):
        csv_parser = FileParser("Transit Ticket input 1.csv")
        violations_to_compare = [
            TrafficViolation(
                IdentityCard(
                    name="Josevaldo Cal. O. Teiro", number="467191153"
                ),
                LicensePlate('ARE-9420')
            ),
            TrafficViolation(
                IdentityCard(
                    name="Josevaldo Cal. O. Teiro", number="467191153"
                ),
                LicensePlate('KVI-2310')
            ),
            TrafficViolation(
                IdentityCard(
                    name="Josevaldo Cal. O. Teiro", number="467191153"
                ),
                LicensePlate('KVI-2310')
            ),
            TrafficViolation(
                IdentityCard(
                    name="Josevaldo Cal. O. Teiro", number="467191153"
                ),
                LicensePlate('ARE-9420')
            ),
            TrafficViolation(
                IdentityCard(
                    name="Osvaldo Plinio", number="276787067"
                ),
                LicensePlate('BIO-9626')
            ),
            TrafficViolation(
                IdentityCard(
                    name="Gerusa Juventina", number="149178360"
                ),
                LicensePlate('SOS-3257')
            )
        ]

        traffic_violations = csv_parser.traffic_violations()

        self.assertEqual(traffic_violations, violations_to_compare)
