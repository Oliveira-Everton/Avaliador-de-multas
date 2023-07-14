import unittest

from main_penalty_calculate.models import TypeInfraction


class TestTypeInfraction(unittest.TestCase):
    def test_type_infraction(self):
        type_infraction = TypeInfraction('Gravíssima')

        type = type_infraction.type

        self.assertEqual(type, 'Gravíssima')
