class OutputSerializer:

    def __init__(self, traffic_violation_model):
        self._model = traffic_violation_model
        self._output = []

    def _output_id(self):
        for model in self._model.id_cards:
            self._output.append(
                f'{model.number}; {model.name}'
            )

    def _output_plate(self):
        for model in self._model.license_plates:
            self._output.append(
                f'{model.number}'
            )

    def output_string(self):
        self._output_id()
        self._output_plate()
        return self._output
