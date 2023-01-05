import csv

from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.license_plate import LicensePlate
from penalty_calculate.models.traffic_violation import TrafficViolation
from penalty_calculate.models.traffic_violations import TrafficViolations
from penalty_calculate.serializers.output_serializer import OutputSerializer


class FileParser:

    _IDENTITY_NAME = -1
    _IDENTITY_NUMBER = 5
    _LICENSE_PLATE = 0

    def __init__(self, file_name):
        self._file_name = file_name
        self._csv_file = self._serialize_file()

    def _serialize_file(self):
        with open(self._file_name, mode="r") as file:
            reader_csv = csv.reader(file, delimiter=";")
            return list(enumerate(reader_csv))

    def _build_traffic_violation_models(self):
        traffic_violations = []
        for line, column in self._csv_file:
            if line != 0:
                traffic_violations.append(
                    TrafficViolation(
                        IdentityCard(
                            name=column[self._IDENTITY_NAME],
                            number=column[self._IDENTITY_NUMBER]
                        ),
                        LicensePlate(
                            number=column[self._LICENSE_PLATE]
                        )
                    )
                )
        self._traffic_violations = traffic_violations

    def output_file(self):
        self._build_traffic_violation_models()
        traffic_violations = TrafficViolations(self._traffic_violations)
        output_string = OutputSerializer(traffic_violations).output_string()
        return output_string
