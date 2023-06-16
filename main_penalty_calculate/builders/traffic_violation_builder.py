from ..models import TrafficViolation, IdentityCard, LicensePlate


class TrafficViolationBuilder:
    _IDENTITY_NAME = 6
    _IDENTITY_NUMBER = 5
    _LICENSE_PLATE = 0
    _FIRST_LINE = 0

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
                        )
                    )
                )
        return traffic_violations
