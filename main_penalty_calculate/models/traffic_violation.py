class TrafficViolation:
    def __init__(self, identity_card, license_plate):
        self._identity_card = identity_card
        self._license_plate = license_plate

    @property
    def identity_card_number(self):
        return self._identity_card.number

    @property
    def identity_card_name(self):
        return self._identity_card.name

    @property
    def license_plate_number(self):
        return self._license_plate.number

    def _compare_properties(self, traffic_violation):
        return [
            traffic_violation.identity_card_name,
            traffic_violation.identity_card_number,
            traffic_violation.license_plate_number        ]

    def __eq__(self, other):
        return self._compare_properties(self) == self._compare_properties(other)
