import csv

from penalty_calculate.models.identity_cards import IdentityCards


class FileParser:
    def __init__(self, file_name):
        self._file_name = file_name
        self._csv_file = self._open_file()

    def _open_file(self):
        with open(self._file_name, mode="r") as file:
            reader_csv = csv.reader(file, delimiter=";")
            return list(enumerate(reader_csv))

    def _take_national_name_and_number_identity_cards(self):
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
        if national_name_identity_cards and national_number_identity_cards:
            return True
        else:
            return False

    def take_national_identity_cards(self):
        self._take_national_name_and_number_identity_cards()
        national_number_and_name_identity_cards = []
        list = []
        for line_numbers, number_identity_cards in enumerate(
            self._identity_cards.check_numbers()
        ):
            for line_names, name_identity_cards in enumerate(
                self._identity_cards.check_names()
            ):
                list.clear()
                if line_numbers == line_names:
                    list.append(number_identity_cards)
                    list.append(name_identity_cards)
# Parei aqui!!! Pensando como usar meu modelo de dados pra me ajudar!
                    national_number_and_name_identity_cards.append(list.copy())
        return national_number_and_name_identity_cards

    def take_license_plate(self):
        license_plate = []
        for line, column in self._csv_file:
            if line != 0:
                license_plate.append(column[0])
        return license_plate

    def take_id_cards_with_license_plate(self):
        national_identity_cards = self.take_national_identity_cards()
        national_identity_cards.append(self.take_license_plate())
        return national_identity_cards
