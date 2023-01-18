class OutputSerializer:
    _OFFENDER_DATA = '{0}; {1}; {2}'

    def __init__(self, traffic_violations):
        self._traffic_violations = traffic_violations

    def _output(self):
        offender_data = []
        for violation in self._traffic_violations:
            self._violation = violation
            offender_data.append(
                self._OFFENDER_DATA.format(
                    self._identity_card.number,
                    self._identity_card.name,
                    self._license_plate.number
                )
            )
        return offender_data

    def output_string(self):
        return self._output()

    @property
    def _identity_card(self):
        return self._violation.identity_card

    @property
    def _license_plate(self):
        return self._violation.license_plate
