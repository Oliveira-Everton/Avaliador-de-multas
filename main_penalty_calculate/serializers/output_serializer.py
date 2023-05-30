class OutputSerializer:
    _OFFENDER_DATA = '{0}; {1}; {2}'

    def __init__(
        self,
        violators_avaliations
    ):
        self._violators_avaliations = violators_avaliations

    def output_string(
        self
    ):
        offender_data = []
        for violation in self._violators_avaliations:
            offender_data.append(
                self._OFFENDER_DATA.format(
                    violation.identity_card_number,
                    violation.identity_card_name,
                    self._unpacks_list(
                        str(
                            violation.license_plate_numbers
                        )
                    )
                )
            )
        return offender_data

    def _unpacks_list(self, text_list):
        unpacked_text = (
            text_list[:].replace(
                "[", ""
            )
        )[:].replace(
            "]", ""
        )
        return unpacked_text.replace("'", '')

    def _removes_quotes(self, text):
        return text
    