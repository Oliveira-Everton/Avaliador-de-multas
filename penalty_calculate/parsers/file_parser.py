import csv

from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.license_plate import LicensePlate
from penalty_calculate.models.traffic_violation import TrafficViolation


class FileParser:

    _IDENTITY_NAME = -1
    _IDENTITY_NUMBER = 5
    _LICENSE_PLATE = _FIRST_LINE = 0
    _READ = 'r'
    _SEMICOLON = ';'

    def __init__(self, file_name):
        self._csv_file = self._convert_file(file_name)

    def _convert_file(self, file_name):
        with open(file_name, mode=self._READ) as file:
            reader_csv = csv.reader(file, delimiter=self._SEMICOLON)
            return list(enumerate(reader_csv))

    def _build_traffic_violation_models(self):
        traffic_violations = []
        for line, column in self._csv_file:
            if line != self._FIRST_LINE:
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
        return traffic_violations

    def traffic_violations(self):
        return self._build_traffic_violation_models()