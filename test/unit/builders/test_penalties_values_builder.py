import unittest

from datetime import datetime

from main_penalty_calculate.builders import PenaltiesValuesBuilder
from main_penalty_calculate.constants import TypeInfractionStrings
from main_penalty_calculate.models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate
)


class TestPenaltiesValuesBuilder(unittest.TestCase):
    def test_convert_demerit_points_light(self):
        infraction_penalties = PenaltiesValuesBuilder(
            TrafficViolation(
                identity_card=IdentityCard('Morgan', '138469945'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.LIGHT,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            )
        )

        demerit_points_light = infraction_penalties.convert_demerit_points()

        self.assertEqual(demerit_points_light, 3)

    def test_convert_penalty_amount_light(self):
        infraction_penalties = PenaltiesValuesBuilder(
            TrafficViolation(
                identity_card=IdentityCard('Morgan', '138469945'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.LIGHT,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            )
        )

        penalty_amount_light = infraction_penalties.convert_penalty_amount()

        self.assertEqual(penalty_amount_light, 88.38)

    def test_convert_demerit_points_average(self):
        infraction_penalties = PenaltiesValuesBuilder(
            TrafficViolation(
                identity_card=IdentityCard('Morgan', '138469945'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.AVERAGE,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            )
        )

        demerit_points_average = infraction_penalties.convert_demerit_points()

        self.assertEqual(demerit_points_average, 4)

    def test_convert_penalty_amount_average(self):
        infraction_penalties = PenaltiesValuesBuilder(
            TrafficViolation(
                identity_card=IdentityCard('Morgan', '138469945'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.AVERAGE,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            )
        )

        penalty_amount_average = infraction_penalties.convert_penalty_amount()

        self.assertEqual(penalty_amount_average, 130.16)

    def test_convert_demerit_points_serious(self):
        infraction_penalties = PenaltiesValuesBuilder(
            TrafficViolation(
                identity_card=IdentityCard('Morgan', '138469945'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.SERIOUS,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            )
        )

        demerit_points_serious = infraction_penalties.convert_demerit_points()

        self.assertEqual(demerit_points_serious, 5)

    def test_convert_penalty_amount_serious(self):
        infraction_penalties = PenaltiesValuesBuilder(
            TrafficViolation(
                identity_card=IdentityCard('Morgan', '138469945'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.SERIOUS,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            )
        )

        penalty_amount_serious = infraction_penalties.convert_penalty_amount()

        self.assertEqual(penalty_amount_serious, 195.23)

    def test_convert_demerit_points_very_serious(self):
        infraction_penalties = PenaltiesValuesBuilder(
            TrafficViolation(
                identity_card=IdentityCard('Morgan', '138469945'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.VERY_SERIOUS,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            )
        )

        demerit_points_very_serious = (
            infraction_penalties.convert_demerit_points()
        )

        self.assertEqual(demerit_points_very_serious, 7)

    def test_convert_penalty_amount_very_serious(self):
        infraction_penalties = PenaltiesValuesBuilder(
            TrafficViolation(
                identity_card=IdentityCard('Morgan', '138469945'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.VERY_SERIOUS,
                infraction_date=datetime(1999, 1, 3, 12),
                notification_date=datetime(1999, 1, 4, 7)
            )
        )

        penalty_amount_very_serious = (
            infraction_penalties.convert_penalty_amount()
        )

        self.assertEqual(penalty_amount_very_serious, 293.47)

    def test_convert_demerit_points_30th_infrigement_period(self):
        infraction_penalties = PenaltiesValuesBuilder(
            TrafficViolation(
                identity_card=IdentityCard('Morgan', '138469945'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.VERY_SERIOUS,
                infraction_date=datetime(1999, 1, 1, 12),
                notification_date=datetime(1999, 2, 1, 7)
            )
        )

        demerit_points = infraction_penalties.convert_demerit_points()

        self.assertEqual(demerit_points, 7)

    def test_convert_demerit_points_31th_infrigement_period(self):
        infraction_penalties = PenaltiesValuesBuilder(
            TrafficViolation(
                identity_card=IdentityCard('Morgan', '138469945'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.VERY_SERIOUS,
                infraction_date=datetime(1999, 1, 1, 12),
                notification_date=datetime(1999, 2, 2, 7)
            )
        )

        invalid_demerit_points = infraction_penalties.convert_demerit_points()

        self.assertEqual(invalid_demerit_points, 0)

    def test_convert_penalty_amount_30th_infrigement_period(self):
        infraction_penalties = PenaltiesValuesBuilder(
            TrafficViolation(
                identity_card=IdentityCard('Morgan', '138469945'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.VERY_SERIOUS,
                infraction_date=datetime(1999, 1, 1, 12),
                notification_date=datetime(1999, 2, 1, 7)
            )
        )

        penalty_amount = infraction_penalties.convert_penalty_amount()

        self.assertEqual(penalty_amount, 293.47)

    def test_convert_penalty_amount_31th_infrigement_period(self):
        infraction_penalties = PenaltiesValuesBuilder(
            TrafficViolation(
                identity_card=IdentityCard('Morgan', '138469945'),
                license_plate=LicensePlate('MGN-9130'),
                type_infraction=TypeInfractionStrings.VERY_SERIOUS,
                infraction_date=datetime(1999, 1, 1, 12),
                notification_date=datetime(1999, 2, 2, 7)
            )
        )

        invalid_penalty_amount = infraction_penalties.convert_penalty_amount()

        self.assertEqual(invalid_penalty_amount, 0.0)
