from .parsers.file_parser import FileParser


class PenaltyCalculate:

    def __init__(self, csv_file):
        self._csv_file = csv_file
    
    def csv_reader(self):
        csv_file = FileParser(self._csv_file).take_national_identity_cards_with_license_plate()
        return csv_file
