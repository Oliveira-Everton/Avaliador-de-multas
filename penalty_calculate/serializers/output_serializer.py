class OutputSerializer:
    _OFFENDER_DATA = '{0}; {1}; {2}'

    def __init__(self, traffic_violations):
        self._output_identity_cards(traffic_violations)

    def _output_identity_cards(self, traffic_violations):
        offender_data = []
        for violation in traffic_violations:
            offender_data.append(
                self._OFFENDER_DATA.format(
                    violation.identity_card.number,
                    violation.identity_card.name,
                    violation.license_plate.number
                )
            )
        self._offender_data = offender_data

    def output_string(self):
        return self._offender_data
