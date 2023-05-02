class TrafficViolation:

    def __init__(self, identity_card, license_plate):
        self._identity_card = identity_card
        self._license_plate = license_plate

    @property
    def identity_card(self):
        return self._identity_card

    @property
    def license_plate(self):
        return self._license_plate

    def __eq__(self, other):
        identity_cards_equals = \
            self._identity_card.number == other._identity_card.number
        license_plates_equals = \
            self._license_plate.number == other._license_plate.number
        return identity_cards_equals == license_plates_equals
