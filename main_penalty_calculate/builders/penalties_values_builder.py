from ..constants import TypeInfractionStrings


class PenaltiesValuesBuilder:
    _DEMERIT_POINTS = 'demerit_points'
    _PENALTY_AMOUNT = 'penalty_amount'
    _INVALID_DEMERIT_POINTS = 0
    _VALIDITY_PERIOD_OF_INFRINGEMENT = 30
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

    def __init__(self, traffic_violation):
        self._traffic_violation = traffic_violation

    def _is_demerit_points_valid(self):
        return (
            self._traffic_violation.notification_date -
            self._traffic_violation.infraction_date
        ).days <= self._VALIDITY_PERIOD_OF_INFRINGEMENT

    def convert_demerit_points(self):
        if self._is_demerit_points_valid():
            return self._INFRACTION_PENALTIES[
                self._traffic_violation.type_infraction
            ][self._DEMERIT_POINTS]
        else:
            return self._INVALID_DEMERIT_POINTS

    def convert_penalty_amount(self):
        return self._INFRACTION_PENALTIES[
            self._traffic_violation.type_infraction
        ][self._PENALTY_AMOUNT]
