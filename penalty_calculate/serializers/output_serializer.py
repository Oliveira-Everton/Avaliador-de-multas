class OutputSerializer:

    def __init__(self, traffic_violation_model):
        self._traffic_violation_model = traffic_violation_model
        self._output = []

    def _output_id_cards(self):
        for model in self._traffic_violation_model.id_cards:
            self._output.append(
                f'{model.number}; {model.name}'
            )

    def _output_license_plates(self):
        for model in self._traffic_violation_model.license_plates:
            self._output.append(
                f'{model.number}'
            )

    def output_string(self):
        self._output_id_cards()
        self._output_license_plates()
        return self._output
