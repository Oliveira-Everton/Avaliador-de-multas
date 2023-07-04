import csv


class FileParser:
    _READ_PARAMETER = 'r'
    _DELIMITER = ';'
    _UNICODE = 'utf-8'
    _IDENTITY_CARD_NAME_KEY = 'identity_card_name'
    _IDENTITY_CARD_NUMBER_KEY = 'identity_card_number'
    _LICENSE_PLATE_NUMBER_KEY = 'license_plate_number'
    _TYPE_INFRACTION_KEY = 'type_infraction'
    _INFRACTION_DATE_KEY = 'infraction_date'
    _NOTIFICATION_DATE_KEY = 'notification_date'
    _IDENTITY_CARD_NAME_INDEX = -1
    _IDENTITY_CARD_NUMBER_INDEX = 5
    _LICENSE_PLATE_INDEX = 0
    _FIRST_LINE_INDEX = 0
    _TYPE_INFRACTION_INDEX = 1
    _INFRACTION_DATE_INDEX = 2
    _NOTIFICATION_DATE_INDEX = 3

    def __init__(self, file_name):
        self._file_name = file_name

    def _convert_file(self):
        with open(
            self._file_name,
            mode=self._READ_PARAMETER,
            encoding=self._UNICODE
        ) as file:
            reader_csv = csv.reader(file, delimiter=self._DELIMITER)
            return list(enumerate(reader_csv))

    def pre_traffic_violations(self):
        pre_traffic_violations = []
        for line, column in self._convert_file():
            if line != self._FIRST_LINE_INDEX:
                pre_traffic_violations.append(
                    {
                        self._IDENTITY_CARD_NAME_KEY: column[
                            self._IDENTITY_CARD_NAME_INDEX
                        ],
                        self._IDENTITY_CARD_NUMBER_KEY: column[
                            self._IDENTITY_CARD_NUMBER_INDEX
                        ],
                        self._LICENSE_PLATE_NUMBER_KEY: column[
                            self._LICENSE_PLATE_INDEX
                        ],
                        self._TYPE_INFRACTION_KEY: column[
                            self._TYPE_INFRACTION_INDEX
                        ],
                        self._INFRACTION_DATE_KEY: column[
                            self._INFRACTION_DATE_INDEX
                        ],
                        self._NOTIFICATION_DATE_KEY: column[
                            self._NOTIFICATION_DATE_INDEX
                        ]
                    }
                )
        return pre_traffic_violations
