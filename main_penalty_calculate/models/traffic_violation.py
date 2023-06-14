class TrafficViolation:
    def __init__(
        self,
        identity_card,
        license_plate
    ):
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

    def _properties_values(self):
        return [
            self.identity_card_number,
            self.identity_card_name,
            self.license_plate_number
        ]

    def __eq__(self, other):
        return (
            self._properties_values() == other._properties_values()
        )
