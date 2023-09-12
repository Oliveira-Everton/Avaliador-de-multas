import re


class OutputSerializer:
    _OFFENDER_DATA = (
        '{violation.identity_card.number}; '
        '{violation.identity_card.name}; '
        '{license_plate_numbers}; '
        '{violation.demerit_points}; '
        '{violation.penalty_amount:.2f}'
    )
    _STRINGS_TO_BE_REPLACED = r'\[|\]|\''
    _REPLACEMENT_STRING = ''
    _LINE_BREAK_TO_NEXT_OFFENDER = '\n'

    def __init__(self, violators_avaliations):
        self._violators_avaliations = violators_avaliations

    def _build_offenders_data(self):
        offenders_data = []
        for violation in self._violators_avaliations:
            offenders_data.append(
                self._OFFENDER_DATA.format(
                    violation=violation,
                    license_plate_numbers=re.sub(
                        self._STRINGS_TO_BE_REPLACED,
                        self._REPLACEMENT_STRING,
                        self._convert_license_plates_strings(
                            violation.license_plate_numbers
                        )
                    )
                )
            )
        return offenders_data

    def _convert_license_plates_strings(self, license_plates):
        license_plates_strings = []
        for license_plate in license_plates:
            license_plates_strings.append(license_plate.number)
        return str(license_plates_strings)

    def output_string(self):
        offenders_datas = self._build_offenders_data()
        return self._LINE_BREAK_TO_NEXT_OFFENDER.join(offenders_datas)
