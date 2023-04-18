class OutputSerializer:
    _OFFENDER_DATA = '{0}; {1}; {2}; {3}; {4}; {5}'

    def __init__(self, traffic_violations):
        self._traffic_violations = traffic_violations

    def output_string(self):
        offender_data = []
        for violation in self._traffic_violations:
            offender_data.append(
                self._OFFENDER_DATA.format(
                    violation.identity_card_number,
                    violation.identity_card_name,
                    violation.license_plate_number,
                    violation.type_infraction,
                    violation.infraction_date,
                    violation.notification_date
                )
            )
        return offender_data
