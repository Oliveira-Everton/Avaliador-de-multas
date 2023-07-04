from .parsers import FileParser
from .serializers import OutputSerializer
from .builders import ViolatorsAvaliationsBuilder, TrafficViolationBuilder


class PenaltyCalculate:
    def __init__(self, file_name):
        self._file_name = file_name

    def evaluate_infractors(self):
        pre_traffic_violations = FileParser(
            self._file_name
        ).pre_traffic_violations()
        traffic_violations = TrafficViolationBuilder(
            pre_traffic_violations
        ).build_traffic_violations()
        violators_avaliations = ViolatorsAvaliationsBuilder(
            traffic_violations
        ).build_violators_avaliations()
        return OutputSerializer(violators_avaliations).output_string()
