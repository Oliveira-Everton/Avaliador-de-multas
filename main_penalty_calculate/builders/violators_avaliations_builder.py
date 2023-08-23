from ..models import ViolatorAvaliation, InfractionPenalties


class ViolatorsAvaliationsBuilder:
    _VALIDITY_PERIOD_OF_INFRINGEMENT = 30
    _INVALID_DEMERIT_POINTS = 0
    _DEMERIT_POINTS_INDEX = 0
    _PENALTY_AMOUNT_INDEX = 1

    def __init__(self, traffic_violations):
        self._traffic_violations = traffic_violations
        self._violators_avaliations = []

    def _is_identity_card_already_present(self, traffic_violation):
        for violator_avaliation in self._violators_avaliations:
            if (
                violator_avaliation.identity_card ==
                traffic_violation.identity_card
            ):
                return True
        return False

    def _is_license_plate_already_present(
        self,
        license_plates,
        traffic_violation
    ):
        for license_plate in license_plates:
            if (
                license_plate ==
                traffic_violation.license_plate
            ):
                return True
        return False

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
            return InfractionPenalties(type_infraction).demerit_points
        else:
            return self._INVALID_DEMERIT_POINTS

    def _convert_penalty_amount(self, type_infraction):
        return InfractionPenalties(type_infraction).penalty_amount

    def _aggregate_license_plates(
        self,
        violator_avaliation,
        traffic_violation
    ):
        if not self._is_license_plate_already_present(
            violator_avaliation.license_plate_numbers,
            traffic_violation
        ):
            violator_avaliation.license_plate_numbers.append(
                traffic_violation.license_plate
            )

    def _aggregate_demerit_points(
        self,
        violator_avaliation,
        traffic_violation
    ):
        violator_avaliation.sum_demerit_points(
            self._convert_demerit_points(
                traffic_violation.notification_date,
                traffic_violation.infraction_date,
                traffic_violation.type_infraction
            )
        )

    def _aggregate_penalty_amount(
        self,
        violator_avaliation,
        traffic_violation
    ):
        violator_avaliation.sum_penalty_amount(
            self._convert_penalty_amount(
                traffic_violation.type_infraction
            )
        )

    def _aggregate_values_by_identity_card(self, traffic_violation):
        for violator_avaliation in self._violators_avaliations:
            if (
                violator_avaliation.identity_card ==
                traffic_violation.identity_card
            ):
                self._aggregate_license_plates(
                    violator_avaliation,
                    traffic_violation
                )
                self._aggregate_demerit_points(
                    violator_avaliation,
                    traffic_violation
                )
                self._aggregate_penalty_amount(
                    violator_avaliation,
                    traffic_violation
                )

    def build_violators_avaliations(self):
        for traffic_violation in self._traffic_violations:
            if self._is_identity_card_already_present(
                traffic_violation
            ):
                self._aggregate_values_by_identity_card(
                    traffic_violation
                )
            else:
                self._violators_avaliations.append(
                    ViolatorAvaliation(
                        identity_card=traffic_violation.identity_card,
                        license_plates=[traffic_violation.license_plate],
                        demerit_points=self._convert_demerit_points(
                            traffic_violation.notification_date,
                            traffic_violation.infraction_date,
                            traffic_violation.type_infraction
                        ),
                        penalty_amount=self._convert_penalty_amount(
                            traffic_violation.type_infraction
                        )
                    )
                )
        return self._violators_avaliations
