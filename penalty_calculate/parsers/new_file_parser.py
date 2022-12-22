import csv

from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.license_plates import LicensePlates
from penalty_calculate.managers.new_id_cards_manager import NewIdCardsManager


class NewFileParser:

    _IDENTITY_NAME = -1
    _IDENTITY_NUMBER = 5

    def __init__(self, file_name):
        self._file_name = file_name
        self._csv_file = self._open_file()

    def _open_file(self):
        with open(self._file_name, mode="r") as file:
            reader_csv = csv.reader(file, delimiter=";")
            return list(enumerate(reader_csv))

    def _take_name_and_number_identity_cards(self):
        models_id = []
        for line, column in self._csv_file:
            if line != 0:
                identit_card = IdentityCard(
                    id_name=column[self._IDENTITY_NAME],
                    id_number=column[self._IDENTITY_NUMBER]
                )
                models_id.append(identit_card)
        return models_id
    # retorna uma lista com vários modelos de dados
    # que tem como atributos RG e Nome

    def take_national_identity_cards(self):
        models_id_cards = self._take_name_and_number_identity_cards()
        id_cards = NewIdCardsManager(models_id_cards)._analyze_models
    

        
