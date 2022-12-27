import csv

from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.license_plates import LicensePlates
from penalty_calculate.managers.new_id_cards_manager import NewIdCardsManager
from penalty_calculate.models.traffic_violation import TrafficViolation


class NewFileParser:

    _IDENTITY_NAME = -1
    _IDENTITY_NUMBER = 5
    _LICENSE_PLATE = _MODELS_ID = 0
    _MODELS_PLATES = 1

    def __init__(self, file_name):
        self._file_name = file_name
        self._csv_file = self._open_file()

    def _open_file(self):
        with open(self._file_name, mode="r") as file:
            reader_csv = csv.reader(file, delimiter=";")
            return list(enumerate(reader_csv))

    def _organize_models(self):
        models_id = []
        models_plate = []
        for line, column in self._csv_file:
            if line != 0:
                identity_card = IdentityCard(
                    id_name=column[self._IDENTITY_NAME],
                    id_number=column[self._IDENTITY_NUMBER]
                )
                license_plate = LicensePlates(
                    column[self._LICENSE_PLATE]
                )
                models_id.append(identity_card)
                models_plate.append(license_plate)
        return (models_id, models_plate)

    def _take_national_identity_cards(self):
        self._models_id_cards = self._organize_models()[self._MODELS_ID]
        # Quando uma classe tem um retorno como um objeto ou um modelo de dados
        # como testar se deu certo com um assertEqual?

    def _take_license_plate(self):
        self._models_license_plates = self._organize_models()[self._MODELS_PLATES]

# Agora provavelmente esse cara vai chamar o TrafficViolation
# E depois o OutputSerializer...O que vc acha?
