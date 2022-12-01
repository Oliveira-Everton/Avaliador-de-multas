import csv

class FileManager:
    def __init__(self, file_name):
        self._file_name = file_name
    
    def _open_file(self):
        with open(self._file_name, mode="r") as file:
            reader_csv = csv.reader(file, delimiter=";")
            return list(enumerate(reader_csv))

    def _take_national_number_identity_cards(self):
        national_number_identity_cards = []
        for line, column in self._open_file():
                if line != 0:
                    national_number_identity_cards.append(column[5])
        return national_number_identity_cards

    def _take_national_name_identity_cards(self):
        national_name_identity_cards = []
        for line, column in self._open_file():
            if line != 0:
                national_name_identity_cards.append(column[-1])
        return national_name_identity_cards

    def take_national_identity_cards(self):
        national_number_and_name_identity_cards = []
        list = []
        for line_numbers, number_identity_cards in enumerate(self._take_national_number_identity_cards()):
            for line_names, name_identity_cards in enumerate(self._take_national_name_identity_cards()):
                list.clear()
                if line_numbers == line_names:
                    list.append(number_identity_cards)
                    list.append(name_identity_cards)
                    national_number_and_name_identity_cards.append(list.copy())
        return national_number_and_name_identity_cards

    def _take_license_plate(self):
        license_plate = []
        for line, column in self._open_file():
            if line != 0:
                license_plate.append(column[0])
        return license_plate
    
    def take_national_identity_cards_with_license_plate(self):
        national_identity_cards = self.take_national_identity_cards()
        license_plates = self._take_license_plate()
        national_identity_cards.append(license_plates)
        return license_plates
