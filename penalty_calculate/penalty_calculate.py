from .parsers.file_parser import FileParser


class PenaltyCalculate:

    def __init__(self, csv_file):
        self._csv_file = csv_file

    def csv_reader(self):
        file_parser = FileParser(self._csv_file)
        output_string = file_parser.output_file()
        return output_string
