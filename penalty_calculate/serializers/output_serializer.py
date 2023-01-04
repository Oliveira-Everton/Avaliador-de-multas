class OutputSerializer:

    def __init__(self, violations_manager):
        self._traffic_violations = violations_manager.traffic_violations
        self._output = []

    def _output_id_cards(self):
        for violation in self._traffic_violations:
            self._output.append(
                f'{violation.id_card.number}; {violation.id_card.name}'
            )

    def _output_license_plates(self):
        for violation in self._traffic_violations:
            self._output.append(
                f'{violation.license_plate.number}'
            )

    def output_string(self):
        self._output_id_cards()
        self._output_license_plates()
        return self._output
