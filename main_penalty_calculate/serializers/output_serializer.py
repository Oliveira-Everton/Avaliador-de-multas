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
            plates = str(violation.license_plate_numbers).replace("]", "")
            offender_data.append(
                self._OFFENDER_DATA.format(
                    violation.identity_card_number,
                    violation.identity_card_name,
                    plates.replace("[", "")
                )
            )
        return offender_data
