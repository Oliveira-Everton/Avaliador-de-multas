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
    def license_plate(self):
        return self._license_plate.number

    def __eq__(self, other):
        return (
            self.identity_card_number == other.identity_card_number,
            self.license_plate == other.license_plate
        )
