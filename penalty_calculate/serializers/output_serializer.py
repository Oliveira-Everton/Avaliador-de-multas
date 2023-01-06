class OutputSerializer:

    def __init__(self, traffic_violations):
        self._traffic_violations = traffic_violations.traffic_violations
        self._output = []

    def _output_identity_cards(self):
        for violation in self._traffic_violations:
            self._output.append(
                f'{violation.identity_card.number}; {violation.identity_card.name}'
            )

    def _output_license_plates(self):
        for violation in self._traffic_violations:
            self._output.append(
                f'{violation.license_plate.number}'
            )

    def output_string(self):
        self._output_identity_cards()
        self._output_license_plates()
        return self._output
