from .parsers import FileParser
from .managers import ViolationsManager
from .serializers import OutputSerializer


class PenaltyCalculate:
    def __init__(self, file_name):
        self._file_name = file_name

    def _csv_reader(self):
        return FileParser(
            self._file_name
        ).build_traffic_violations()

    def evaluates_infractors(self):
        violators_avaliations = ViolationsManager(
            self._csv_reader()
        ).build_violator_avaliation()
        return OutputSerializer(violators_avaliations).output_string()
