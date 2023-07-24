from datetime import datetime

from ..models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate
)
from ..constants import PenaltyStrings


class TrafficViolationBuilder:
    _IDENTITY_NAME = 6
    _IDENTITY_NUMBER = 5
    _LICENSE_PLATE = 0
    _FIRST_LINE = 0
    _TYPE_INFRACTION = 1
    _INFRACTION_DATE = 2
    _NOTIFICATION_DATE = 3
    _DEGREES_OF_PENALTY = {
        'Leve': PenaltyStrings.LIGHT,
        'Média': PenaltyStrings.AVERAGE,
        'Grave': PenaltyStrings.SERIOUS,
        'Gravíssima': PenaltyStrings.VERY_SERIOUS
    }

    def __init__(self, file):
        self._file = file

    def build_traffic_violations(self):
        traffic_violations = []
        for line, column in self._file:
            if line != self._FIRST_LINE:
                traffic_violations.append(
                    TrafficViolation(
                        identity_card=IdentityCard(
                            name=column[self._IDENTITY_NAME],
                            number=column[self._IDENTITY_NUMBER]
                        ),
                        license_plate=LicensePlate(
                            number=column[self._LICENSE_PLATE]
                        ),
                        type_infraction=self._DEGREES_OF_PENALTY[
                            column[self._TYPE_INFRACTION]
                        ],
                        infraction_date=datetime.fromisoformat(
                            column[self._INFRACTION_DATE]
                        ),
                        notification_date=datetime.fromisoformat(
                            column[self._NOTIFICATION_DATE]
                        )
                    )
                )
        return traffic_violations
