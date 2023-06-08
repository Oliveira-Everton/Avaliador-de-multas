from ..models import (
    ViolatorAvaliation,
    IdentityCard
)


class ViolatorsAvaliationsBuilder:
    _LICENSE_PLATE_IN_LIST = 0
    _FIRST_TRAFFIC_VIOLATION = 0

    def __init__(self, traffic_violations):
        self._traffic_violations = traffic_violations

    def _search_identity_card_number(
        self,
        id_card_number,
        violators_list
    ):
        for violators in violators_list:
            if violators.identity_card_number == id_card_number:
                return True
        return False

    def _search_license_plate_number(
        self,
        license_plate_number,
        violators_list
    ):
        for violators in violators_list:
            if violators == license_plate_number:
                return True
        return False

    def _agroup_license_plates(
        self,
        license_plate_to_be_checked,
        violators_list
    ):
        for violator in violators_list:
            if not self._search_license_plate_number(
                license_plate_to_be_checked,
                violator.license_plate_numbers
            ):
                violator.license_plate_numbers.append(
                    license_plate_to_be_checked
                )

    def build_violators_avaliations(self):
        violators_avaliations = []
        for traffic_violation in self._traffic_violations:
            if self._search_identity_card_number(
                traffic_violation.identity_card_number,
                violators_avaliations
            ):
                self._agroup_license_plates(
                    traffic_violation.license_plate_number,
                    violators_avaliations
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
                        ]
                    )
                )
        return violators_avaliations
