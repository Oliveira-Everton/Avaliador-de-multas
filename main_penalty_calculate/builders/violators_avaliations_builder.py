from ..models import (
    ViolatorAvaliation,
    IdentityCard
)


class ViolatorsAvaliationsBuilder:
    def __init__(self, traffic_violations):
        self._traffic_violations = traffic_violations
        self._violators_avaliations = []

    def _agroup_violators_avaliations(self):
        revised_violators = []
        for violator in self._violators_avaliations:
            uniq = True
            for revised_violator in revised_violators:
                if violator.identity_card_number == \
                        revised_violator.identity_card_number:
                    uniq = False
                    if violator.license_plate_numbers[0] not in \
                            revised_violator.license_plate_numbers:
                        revised_violator.license_plate_numbers.append(
                            violator.license_plate_numbers[0]
                        )
            if uniq:
                revised_violators.append(violator)
        return revised_violators

    def build_violators_avaliations(self):
        for traffic_violation in self._traffic_violations:
            self._violators_avaliations.append(
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
        return self._agroup_violators_avaliations()
