from .parsers import FileParser
from .serializers import OutputSerializer


class PenaltyCalculate:
    def __init__(self, file_name):
        self._file_name = file_name

    def csv_reader(self):
        traffic_violations = FileParser(
            self._file_name
        ).build_traffic_violations()
        return OutputSerializer(traffic_violations).output_string()
