from datetime import datetime

from ..models import ViolatorAvaliation, IdentityCard


class ViolatorsAvaliationsBuilder:
    _LICENSE_PLATE_IN_LIST = 0
    _FIRST_TRAFFIC_VIOLATION = 0
    _DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    _VALIDITY_PERIOD_OF_INFRINGEMENT = 30
    _INVALID_DEMERIT_POINTS = 0
    _INFRACTION_PENALTIES = {
        'Leve': 3,
        'Média': 4,
        'Grave': 5,
        'Gravíssima': 7
    }

    def __init__(self, traffic_violations):
        self._traffic_violations = traffic_violations
        self._violators_avaliations = []

    def _is_identity_card_number_already_present(self):
        for self._violator in self._violators_avaliations:
            if (
                self._violator.identity_card_number ==
                self._traffic_violation.identity_card_number
            ):
                return True
        return False

    def _is_license_plate_number_already_present(
        self,
        license_plate_list
    ):
        for license_plate_number in license_plate_list:
            if (
                license_plate_number ==
                self._traffic_violation.license_plate_number
            ):
                return True
        return False

    def _agroup_license_plates(self):
        if not self._is_license_plate_number_already_present(
            self._violator.license_plate_numbers
        ):
            self._violator.license_plate_numbers.append(
                self._traffic_violation.license_plate_number
            )

    def _aggregate_demerit_points(self):
        self._violator.sum_demerit_points(
            self._INFRACTION_PENALTIES[
                self._traffic_violation.type_infraction
            ]
        )

    def _validate_demerit_points(self):
        if (
            datetime.strptime(
                self._traffic_violation.notification_date,
                self._DATE_FORMAT
            ) -
            datetime.strptime(
                self._traffic_violation.infraction_date,
                self._DATE_FORMAT
            )
        ).days <= self._VALIDITY_PERIOD_OF_INFRINGEMENT:
            return True
        else:
            return False

    def _calculate_demerit_points(self):
        if self._validate_demerit_points():
            return self._INFRACTION_PENALTIES[
                self._traffic_violation.type_infraction
            ]
        else:
            return self._INVALID_DEMERIT_POINTS

    def _aggregate_values_by_identity_card_number(self):
        if self._is_identity_card_number_already_present():
            self._agroup_license_plates()
            if self._validate_demerit_points():
                self._aggregate_demerit_points()

    def build_violators_avaliations(self):
        for self._traffic_violation in self._traffic_violations:
            if self._is_identity_card_number_already_present():
                self._aggregate_values_by_identity_card_number()
            else:
                self._violators_avaliations.append(
                    ViolatorAvaliation(
                        identity_card=IdentityCard(
                            number=(
                                self._traffic_violation.identity_card_number
                            ),
                            name=self._traffic_violation.identity_card_name
                        ),
                        license_plates=[
                            self._traffic_violation.license_plate_number
                        ],
                        demerit_points=self._calculate_demerit_points()
                    )
                )
        return self._violators_avaliations
