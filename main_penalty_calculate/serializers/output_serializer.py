import re


class OutputSerializer:
    _OFFENDER_DATA = (
        '{identity_card.number}; '
        '{identity_card.name}; '
        '{license_plate_numbers}; '
        '{demerit_points}; '
        '{penalty_amount}'
    )
    _PATTERN_FOR_REGEX = r'\[|\]|\''
    _EMPTY_STRING = ''
    _LINE_BREAK = '\n'

    def __init__(self, violators_avaliations):
        self._violators_avaliations = violators_avaliations

    def output_string(self):
        offender_data = []
        for violation in self._violators_avaliations:
            offender_data.append(
                self._OFFENDER_DATA.format(
                    identity_card=violation.identity_card,
                    demerit_points=violation.demerit_points,
                    penalty_amount=violation.penalty_amount,
                    license_plate_numbers=re.sub(
                        self._PATTERN_FOR_REGEX,
                        self._EMPTY_STRING,
                        self._license_plates_strings(
                            violation.license_plate_numbers
                        )
                    )
                )
            )
        return self._LINE_BREAK.join(offender_data)

    def _license_plates_strings(self, license_plates):
        license_plates_strings = []
        for license_plate in license_plates:
            license_plates_strings.append(license_plate.number)
        return str(license_plates_strings)
