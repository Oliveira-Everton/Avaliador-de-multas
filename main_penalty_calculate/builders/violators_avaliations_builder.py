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

    def _is_identity_card_number_already_present(
        self,
        identity_card_number_to_be_checked,
        identity_card_number_list
    ):
        for identity_card in identity_card_number_list:
            if (
                identity_card.identity_card_number ==
                identity_card_number_to_be_checked
            ):
                return True
        return False

    def _is_license_plate_number_already_present(
        self,
        license_plate_number_to_be_checked,
        license_plate_list
    ):
        for license_plate_number in license_plate_list:
            if (
                license_plate_number ==
                license_plate_number_to_be_checked
            ):
                return True
        return False

    def _agroup_license_plates(
        self,
        license_plate_in_review,
        violators_list,
        violator_in_review
    ):
        for violator in violators_list:
            if violator.identity_card_number == violator_in_review:
                if not self._is_license_plate_number_already_present(
                    license_plate_in_review,
                    violator.license_plate_numbers
                ):
                    violator.license_plate_numbers.append(
                        license_plate_in_review
                    )

    def _aggregate_demerit_points(
        self,
        violators_list,
        violator_in_review,
        sum_value
    ):
        for violator in violators_list:
            if violator.identity_card_number == violator_in_review:
                violator.sum_demerit_points(sum_value)

    def _validate_penalty(self, notification_date, infraction_date):
        if (
            datetime.strptime(notification_date, self._DATE_FORMAT) -
            datetime.strptime(infraction_date, self._DATE_FORMAT)
        ).days <= self._VALIDITY_PERIOD_OF_INFRINGEMENT:
            return True
        else:
            return False

    def _calculate_demerit_points(self, traffic_violation):
        if self._validate_penalty(
            traffic_violation.notification_date,
            traffic_violation.infraction_date
        ):
            return self._INFRACTION_PENALTIES[
                traffic_violation.type_infraction
            ]
        else:
            return self._INVALID_DEMERIT_POINTS

    def build_violators_avaliations(self):
        violators_avaliations = []
        for traffic_violation in self._traffic_violations:
            if self._is_identity_card_number_already_present(
                traffic_violation.identity_card_number,
                violators_avaliations,
            ):
                self._agroup_license_plates(
                    traffic_violation.license_plate_number,
                    violators_avaliations,
                    traffic_violation.identity_card_number
                )
                if self._validate_penalty(
                    traffic_violation.notification_date,
                    traffic_violation.infraction_date
                ):
                    self._aggregate_demerit_points(
                        violators_avaliations,
                        traffic_violation.identity_card_number,
                        self._INFRACTION_PENALTIES[
                            traffic_violation.type_infraction
                        ]
                    )
            else:
                violators_avaliations.append(
                    ViolatorAvaliation(
                        identity_card=IdentityCard(
                            number=traffic_violation.identity_card_number,
                            name=traffic_violation.identity_card_name
                        ),
                        license_plates=[
                            traffic_violation.license_plate_number
                        ],
                        demerit_points=self._calculate_demerit_points(
                            traffic_violation
                        )
                    )
                )
        return violators_avaliations
