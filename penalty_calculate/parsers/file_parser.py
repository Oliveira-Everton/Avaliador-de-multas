import csv

from penalty_calculate.models.identity_cards import IdentityCards
from penalty_calculate.models.license_plates import LicensePlates
from penalty_calculate.managers.id_cards_manager import IdCardsManager


class FileParser:
    def __init__(self, file_name):
        self._file_name = file_name
        self._csv_file = self._open_file()

    def _open_file(self):
        with open(self._file_name, mode="r") as file:
            reader_csv = csv.reader(file, delimiter=";")
            return list(enumerate(reader_csv))

    def _take_name_and_number_identity_cards(self):
        national_number_identity_cards = []
        national_name_identity_cards = []
        for line, column in self._csv_file:
            if line != 0:
                national_number_identity_cards.append(column[5])
                national_name_identity_cards.append(column[-1])
        self._identity_cards = IdentityCards(
            identity_numbers=national_number_identity_cards,
            identity_names=national_name_identity_cards
        )

    def take_national_identity_cards(self):
        self._take_name_and_number_identity_cards()
        return IdCardsManager(self._identity_cards).take_id_cards()

    def take_license_plate(self):
        license_plates = []
        for line, column in self._csv_file:
            if line != 0:
                license_plates.append(column[0])
        return LicensePlates(license_plates).check_plates()

    def take_id_cards_with_license_plate(self):
        national_identity_cards = self.take_national_identity_cards()
        national_identity_cards.append(self.take_license_plate())
        return national_identity_cards
