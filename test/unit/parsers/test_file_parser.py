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
                        number="ARE-9420"
                    ),
                    type_infraction="Gravíssima",
                    infraction_date="1999-11-05 15:00:00",
                    notification_date="2000-01-25 10:00:00",
                    pay_date=""
                ),
                TrafficViolation(
                    IdentityCard(
                        name="Josevaldo Cal. O. Teiro",
                        number="467191153"
                    ),
                    LicensePlate(
                        number="KVI-2310"
                    ),
                    type_infraction="Gravíssima",
                    infraction_date="2000-01-01 15:00:00",
                    notification_date="2000-01-04 10:00:00",
                    pay_date=""
                ),
                TrafficViolation(
                    IdentityCard(
                        name="Josevaldo Cal. O. Teiro",
                        number="467191153"
                    ),
                    LicensePlate(
                        number="KVI-2310"
                    ),
                    type_infraction="Grave",
                    infraction_date="2000-01-04 15:00:00",
                    notification_date="2000-01-05 10:00:00",
                    pay_date=""
                ),
                TrafficViolation(
                    IdentityCard(
                        name="Josevaldo Cal. O. Teiro",
                        number="467191153"
                    ),
                    LicensePlate(
                        number="ARE-9420"
                    ),
                    type_infraction="Gravíssima",
                    infraction_date="2000-01-10 15:00:00",
                    notification_date="2000-01-25 10:00:00",
                    pay_date=""
                ),
                TrafficViolation(
                    IdentityCard(
                        name="Osvaldo Plinio",
                        number="276787067"
                    ),
                    LicensePlate(
                        number="BIO-9626"
                    ),
                    type_infraction="Grave",
                    infraction_date="2000-02-05 14:00:00",
                    notification_date="2000-02-10 11:00:00",
                    pay_date=""
                ),
                TrafficViolation(
                    IdentityCard(
                        name="Gerusa Juventina",
                        number="149178360"
                    ),
                    LicensePlate(
                        number="SOS-3257"
                    ),
                    type_infraction="Média",
                    infraction_date="2000-08-16 16:00:00",
                    notification_date="2000-02-11 12:00:00",
                    pay_date=""
                )
            ]
        )
