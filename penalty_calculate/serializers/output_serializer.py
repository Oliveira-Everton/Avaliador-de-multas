class OutputSerializer:
    _OFFENDER_DATA = '{0}; {1}; {2}'

    def __init__(self, traffic_violations):
        self._traffic_violations = traffic_violations

    def _output(self):
        offender_data = []
        for violation in self._traffic_violations:
            offender_data.append(
                self._OFFENDER_DATA.format(
                    violation.identity_card_number,
                    violation.identity_card_name,
                    violation.license_plate_number
                )
            )
        return offender_data

    def output_string(self):
        return self._output()
