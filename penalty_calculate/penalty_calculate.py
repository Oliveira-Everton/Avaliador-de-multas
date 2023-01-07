from .parsers.file_parser import FileParser
from .serializers.output_serializer import OutputSerializer


class PenaltyCalculate:

    def __init__(self, csv_file):
        self._csv_file = csv_file

    def csv_reader(self):
        traffic_violations = FileParser(self._csv_file).traffic_violations()
        return OutputSerializer(traffic_violations).output_string()
