import unittest

from main_penalty_calculate.models import InfractionPenalties
from main_penalty_calculate.constants import TypeInfractionStrings


class TestInfractionPenalties(unittest.TestCase):
    def test_demerit_points_light(self):
        infraction_penalties = InfractionPenalties(
            TypeInfractionStrings.LIGHT
        )

        demerit_points_light = infraction_penalties.demerit_points

        self.assertEqual(demerit_points_light, 3)

    def test_penalty_amount_light(self):
        infraction_penalties = InfractionPenalties(
            TypeInfractionStrings.LIGHT
        )

        penalty_amount_light = infraction_penalties.penalty_amount

        self.assertEqual(penalty_amount_light, 88.38)

    def test_demerit_points_average(self):
        infraction_penalties = InfractionPenalties(
            TypeInfractionStrings.AVERAGE
        )

        demerit_points_average = infraction_penalties.demerit_points

        self.assertEqual(demerit_points_average, 4)

    def test_penalty_amount_average(self):
        infraction_penalties = InfractionPenalties(
            TypeInfractionStrings.AVERAGE
        )

        penalty_amount_average = infraction_penalties.penalty_amount

        self.assertEqual(penalty_amount_average, 130.16)

    def test_demerit_points_serious(self):
        infraction_penalties = InfractionPenalties(
            TypeInfractionStrings.SERIOUS
        )

        demerit_points_serious = infraction_penalties.demerit_points

        self.assertEqual(demerit_points_serious, 5)

    def test_penalty_amount_serious(self):
        infraction_penalties = InfractionPenalties(
            TypeInfractionStrings.SERIOUS
        )

        penalty_amount_serious = infraction_penalties.penalty_amount

        self.assertEqual(penalty_amount_serious, 195.23)

    def test_demerit_points_very_serious(self):
        infraction_penalties = InfractionPenalties(
            TypeInfractionStrings.VERY_SERIOUS
        )

        demerit_points_very_serious = infraction_penalties.demerit_points

        self.assertEqual(demerit_points_very_serious, 7)

    def test_penalty_amount_very_serious(self):
        infraction_penalties = InfractionPenalties(
            TypeInfractionStrings.VERY_SERIOUS
        )

        penalty_amount_very_serious = infraction_penalties.penalty_amount

        self.assertEqual(penalty_amount_very_serious, 293.47)
