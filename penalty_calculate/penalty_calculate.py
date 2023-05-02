from .parsers.file_parser import FileParser
from .serializers.output_serializer import OutputSerializer


class PenaltyCalculate:

    def __init__(self, file_name):
        self._file_name = file_name

    def csv_reader(self):
        traffic_violations = FileParser(self._file_name).traffic_violations()
        return OutputSerializer(traffic_violations).output_string()
