from ..constants import TypeInfractionStrings


class InfractionPenalties:
    _DEMERIT_POINTS = 'demerit_points'
    _PENALTY_AMOUNT = 'penalty_amount'
    _INFRACTION_PENALTIES = {
        TypeInfractionStrings.LIGHT: {
            _DEMERIT_POINTS: 3, _PENALTY_AMOUNT: 88.38
        },
        TypeInfractionStrings.AVERAGE: {
            _DEMERIT_POINTS: 4, _PENALTY_AMOUNT: 130.16
        },
        TypeInfractionStrings.SERIOUS: {
            _DEMERIT_POINTS: 5, _PENALTY_AMOUNT: 195.23
        },
        TypeInfractionStrings.VERY_SERIOUS: {
            _DEMERIT_POINTS: 7, _PENALTY_AMOUNT: 293.47
        }
    }

    def __init__(self, type_infraction):
        self._type_infraction = type_infraction

    @property
    def demerit_points(self):
        return self._INFRACTION_PENALTIES[
            self._type_infraction
        ][self._DEMERIT_POINTS]

    @property
    def penalty_amount(self):
        return self._INFRACTION_PENALTIES[
            self._type_infraction
        ][self._PENALTY_AMOUNT]
