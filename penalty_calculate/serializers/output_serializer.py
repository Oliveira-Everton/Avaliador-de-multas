class OutputSerializer:
    FIRST_ELEMENT = FIRST_LIST = ID_NUMBER = 0
    SECOND_ELEMENT = ID_NAME = 1

    def __init__(self, traffic_violation_model):
        self._model = traffic_violation_model

    def output_id(self):
        id_models = []
        for model in self._model.id_cards:
            id_models.append(
                (model.number, model.name)
            )
        return id_models

    def output_plate(self):
        plates_models = []
        for model in self._model.license_plates:
            plates_models.append(model.number)
        return plates_models

    def output_string(self):
        output = []
        list_models = [self.output_id(), self.output_plate()]
        for index, model in enumerate(list_models):
            if index == self.FIRST_LIST:
                print(model)
        return output
        #USE UM DICIONÁRIO PRA RETORNAR AS LISTAS, TALVEZ AJUDE