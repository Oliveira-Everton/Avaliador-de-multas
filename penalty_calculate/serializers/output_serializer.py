class OutputSerializer:
    _OFFENDER_DATA = '{0}; {1}; {2}'

    def __init__(self, traffic_violations):
        self._traffic_violations = traffic_violations.traffic_violations
        self._output = []

    def _output_identity_cards(self):
        for violation in self._traffic_violations:
            self._output.append(
                self._OFFENDER_DATA.format(
                    violation.identity_card.number,
                    violation.identity_card.name,
                    violation.license_plate.number
                )
            )

    def output_string(self):
        self._output_identity_cards()
        return self._output
