import csv

from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.license_plate import LicensePlate
from penalty_calculate.models.traffic_violation import TrafficViolation
from penalty_calculate.serializers.output_serializer import OutputSerializer


class FileParser:

    _IDENTITY_NAME = -1
    _IDENTITY_NUMBER = 5
    _LICENSE_PLATE = 0

    def __init__(self, file_name):
        self._file_name = file_name
        self._csv_file = self._open_file()

    def _open_file(self):
        with open(self._file_name, mode="r") as file:
            reader_csv = csv.reader(file, delimiter=";")
            return list(enumerate(reader_csv))

    def _organize_models(self):
        list_models_id = []
        list_models_plate = []
        for line, column in self._csv_file:
            if line != 0:
                list_models_id.append(
                    IdentityCard(
                        id_name=column[self._IDENTITY_NAME],
                        id_number=column[self._IDENTITY_NUMBER]
                    )
                )
                list_models_plate.append(
                    LicensePlate(
                        plate_car=column[self._LICENSE_PLATE]
                    )
                )
        self._models_id_cards = list_models_id
        self._models_license_plates = list_models_plate

    def output_file(self):
        self._organize_models()
        traffic_violation = TrafficViolation(
            models_id=self._models_id_cards,
            license_plates=self._models_license_plates
        )
        output_string = OutputSerializer(traffic_violation).output_string()
        return output_string
