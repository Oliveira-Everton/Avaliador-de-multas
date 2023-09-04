from ..models import ViolatorAvaliation
from .penalties_values_builder import PenaltiesValuesBuilder


class ViolatorsAvaliationsBuilder:
    def __init__(self, traffic_violations):
        self._traffic_violations = traffic_violations
        self._violators_avaliations = []

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
            PenaltiesValuesBuilder(
                traffic_violation
            ).convert_demerit_points()
        )

    def _aggregate_penalty_amount(
        self,
        violator_avaliation,
        traffic_violation
    ):
        violator_avaliation.sum_penalty_amount(
            PenaltiesValuesBuilder(
                traffic_violation
            ).convert_penalty_amount()
        )

    def _aggregate_values_by_identity_card(self, traffic_violation):
        for violator_avaliation in self._violators_avaliations:
            if (
                traffic_violation.identity_card ==
                violator_avaliation.identity_card
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
                return True
        return False

    def build_violators_avaliations(self):
        for traffic_violation in self._traffic_violations:
            if not self._aggregate_values_by_identity_card(traffic_violation):
                self._violators_avaliations.append(
                    ViolatorAvaliation(
                        identity_card=traffic_violation.identity_card,
                        license_plates=[traffic_violation.license_plate],
                        demerit_points=PenaltiesValuesBuilder(
                            traffic_violation
                        ).convert_demerit_points(),
                        penalty_amount=PenaltiesValuesBuilder(
                            traffic_violation
                        ).convert_penalty_amount()
                    )
                )
        return self._violators_avaliations
