import re


class OutputSerializer:
    _OFFENDER_DATA = (
        '{violation.identity_card_number}; '\
        '{violation.identity_card_name}; '\
        '{license_plate_numbers}; '\
        '{violation.demerit_points}'
    )
    _PATTERN_FOR_REGEX = r'\[|\]|\''
    _EMPTY_STRING = ''

    def __init__(self, violators_avaliations):
        self._violators_avaliations = violators_avaliations

    def output_string(self):
        offender_data = []
        for violation in self._violators_avaliations:
            offender_data.append(
                self._OFFENDER_DATA.format(
                    violation=violation,
                    license_plate_numbers=re.sub(
                        self._PATTERN_FOR_REGEX,
                        self._EMPTY_STRING,
                        str(violation.license_plate_numbers)
                    )
                )
            )
        return offender_data
