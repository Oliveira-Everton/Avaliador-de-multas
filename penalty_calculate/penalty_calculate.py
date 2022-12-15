from .parsers.file_parser import FileParser


class PenaltyCalculate:

    def __init__(self, csv_file):
        self._csv_file = csv_file

    def csv_reader(self):
        return FileParser(
            self._csv_file
        ).take_id_cards_with_license_plate()
