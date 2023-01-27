class TrafficViolation:
    def __init__(self, identity_card, license_plate):
        self._identity_card_name = identity_card.name
        self._identity_card_number = identity_card.number
        self._license_plate_number = license_plate.number

    @property
    def identity_card_number(self):
        return self._identity_card_number

    @property
    def identity_card_name(self):
        return self._identity_card_name

    @property
    def license_plate_number(self):
        return self._license_plate_number

    def __eq__(self, other):
        return (
            self.identity_card_number == other.identity_card_number,
            self.license_plate_number == other.license_plate_number
        )
