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

    def _is_identity_card_number_already_present(
        self,
        identity_card_number_in_review
    ):
        for violator_avaliation in self._violators_avaliations:
            if (
                violator_avaliation.identity_card_number ==
                identity_card_number_in_review
            ):
                return True
        return False

    def _is_license_plate_number_already_present(
        self,
        license_plate_list,
        license_plate_in_review
    ):
        for license_plate_number in license_plate_list:
            if (
                license_plate_number ==
                license_plate_in_review
            ):
                return True
        return False

    def _aggregate_license_plates(
        self,
        violator_registered,
        license_plate_in_review
    ):
        if not self._is_license_plate_number_already_present(
            violator_registered.license_plate_numbers,
            license_plate_in_review
        ):
            violator_registered.license_plate_numbers.append(
                license_plate_in_review
            )

    def _aggregate_demerit_points(
        self,
        violator_registered,
        notification_date,
        infraction_date,
        type_infraction
    ):
        violator_registered.sum_demerit_points(
            self._convert_demerit_points(
                notification_date,
                infraction_date,
                type_infraction
            )
        )

    def _is_demerit_points_valid(self, notification_date, infraction_date):
        return (
            notification_date - infraction_date
        ).days <= self._VALIDITY_PERIOD_OF_INFRINGEMENT

    def _convert_demerit_points(
        self,
        notification_date,
        infraction_date,
        type_infraction
    ):
        if self._is_demerit_points_valid(notification_date, infraction_date):
            return self._INFRACTION_PENALTIES[type_infraction.type]
        else:
            return self._INVALID_DEMERIT_POINTS

    def _aggregate_values_by_identity_card_number(self, violator_in_review):
        for violator_registered in self._violators_avaliations:
            if (
                violator_registered.identity_card_number ==
                violator_in_review.identity_card_number
            ):
                self._aggregate_license_plates(
                    violator_registered,
                    violator_in_review.license_plate_number
                )
                self._aggregate_demerit_points(
                    violator_registered,
                    violator_in_review.notification_date,
                    violator_in_review.infraction_date,
                    violator_in_review.type_infraction
                )

    def build_violators_avaliations(self):
        for traffic_violation in self._traffic_violations:
            if self._is_identity_card_number_already_present(
                traffic_violation.identity_card_number
            ):
                self._aggregate_values_by_identity_card_number(
                    traffic_violation
                )
            else:
                self._violators_avaliations.append(
                    ViolatorAvaliation(
                        identity_card=IdentityCard(
                            number=(
                                traffic_violation.identity_card_number
                            ),
                            name=traffic_violation.identity_card_name
                        ),
                        license_plates=[
                            traffic_violation.license_plate_number
                        ],
                        demerit_points=self._convert_demerit_points(
                            traffic_violation.notification_date,
                            traffic_violation.infraction_date,
                            traffic_violation.type_infraction
                        )
                    )
                )
        return self._violators_avaliations
