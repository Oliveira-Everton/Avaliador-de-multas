class TrafficViolation:
    def __init__(self, identity_card, license_plate, type_infraction):
        self._identity_card = identity_card
        self._license_plate = license_plate
        self._type_infraction = type_infraction

    @property
    def identity_card_number(self):
        return self._identity_card.number

    @property
    def identity_card_name(self):
        return self._identity_card.name

    @property
    def license_plate_number(self):
        return self._license_plate.number

    @property
    def type_infraction(self):
        return self._type_infraction

    def _compare_properties(self, traffic_violation):
        return [
            traffic_violation.identity_card_name,
            traffic_violation.identity_card_number,
            traffic_violation.license_plate_number,
            traffic_violation.type_infraction
        ]

    def __eq__(self, other):
        return (
            self._compare_properties(self) == self._compare_properties(other)
        )
