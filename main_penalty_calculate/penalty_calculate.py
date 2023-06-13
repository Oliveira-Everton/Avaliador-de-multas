from .parsers import FileParser
from .serializers import OutputSerializer
from .builders import (
    ViolatorsAvaliationsBuilder,
    TrafficViolationBuilder
)


class PenaltyCalculate:
    def __init__(self, file_name):
        self._file_name = file_name

    def evaluate_infractors(self):
        converted_file = FileParser(
            self._file_name
        ).convert_file()
        traffic_violations = TrafficViolationBuilder(
            converted_file
        ).build_traffic_violations()
        violators_avaliations = ViolatorsAvaliationsBuilder(
            traffic_violations
        ).build_violators_avaliations()
        return OutputSerializer(
            violators_avaliations
        ).output_string()
