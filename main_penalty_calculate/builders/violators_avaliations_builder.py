from ..models import ViolatorAvaliation, IdentityCard
from ..constants import TypeInfractionStrings


class ViolatorsAvaliationsBuilder:
    _VALIDITY_PERIOD_OF_INFRINGEMENT = 30
    _INVALID_DEMERIT_POINTS = 0
    _INFRACTION_PENALTIES = {
        TypeInfractionStrings.LIGHT: 3,
        TypeInfractionStrings.AVERAGE: 4,
        TypeInfractionStrings.SERIOUS: 5,
        TypeInfractionStrings.VERY_SERIOUS: 7
    }

    def __init__(self, traffic_violations):
        self._traffic_violations = traffic_violations
        self._violators_avaliations = []

    def _is_identity_card_number_already_present(
        self,
        traffic_violation
    ):
        for violator_avaliation in self._violators_avaliations:
            if (
                violator_avaliation.identity_card_number ==
                traffic_violation.identity_card_number
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
        violator_avaliation,
        license_plate_in_review
    ):
        if not self._is_license_plate_number_already_present(
            violator_avaliation.license_plate_numbers,
            license_plate_in_review
        ):
            violator_avaliation.license_plate_numbers.append(
                license_plate_in_review
            )

    def _aggregate_demerit_points(
        self,
        violator_avaliation,
        notification_date,
        infraction_date,
        type_infraction
    ):
        violator_avaliation.sum_demerit_points(
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
            return self._INFRACTION_PENALTIES[type_infraction]
        else:
            return self._INVALID_DEMERIT_POINTS

    def _aggregate_values_by_identity_card_number(self, traffic_violation):
        for violator_avaliation in self._violators_avaliations:
            if (
                violator_avaliation.identity_card_number ==
                traffic_violation.identity_card_number
            ):
                self._aggregate_license_plates(
                    violator_avaliation,
                    traffic_violation.license_plate_number
                )
                self._aggregate_demerit_points(
                    violator_avaliation,
                    traffic_violation.notification_date,
                    traffic_violation.infraction_date,
                    traffic_violation.type_infraction
                )

    def build_violators_avaliations(self):
        for traffic_violation in self._traffic_violations:
            if self._is_identity_card_number_already_present(
                traffic_violation
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
