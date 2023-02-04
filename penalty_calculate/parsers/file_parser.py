import csv

from ..models import (
    TrafficViolation,
    IdentityCard,
    LicensePlate
)


class FileParser:
    _IDENTITY_NAME = -1
    _IDENTITY_NUMBER = 5
    _LICENSE_PLATE = 0
    _FIRST_LINE = 0
    _READ_PARAMETER = 'r'
    _DELIMITER = ';'

    def __init__(self, file_name):
        self._file_name = file_name

    def _convert_file(self):
        with open(self._file_name, mode=self._READ_PARAMETER) as file:
            reader_csv = csv.reader(file, delimiter=self._DELIMITER)
            return list(enumerate(reader_csv))

    def build_traffic_violations(self):
        traffic_violations = []
        for line, column in self._convert_file():
            if line != self._FIRST_LINE:
                traffic_violations.append(
                    TrafficViolation(
                        identity_card=IdentityCard(
                            name=column[self._IDENTITY_NAME],
                            number=column[self._IDENTITY_NUMBER]
                        ),
                        license_plate=LicensePlate(
                            number=column[self._LICENSE_PLATE]
                        )
                    )
                )
        return traffic_violations
