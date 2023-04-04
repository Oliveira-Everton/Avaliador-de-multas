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

    @property
    def license_plate_type_infraction(self):
        return self._license_plate.type_infraction

    def __eq__(self, other):
        return (
            self.identity_card_name == other.identity_card_name
            and
            self.identity_card_number == other.identity_card_number
            and
            self.license_plate_number == other.license_plate_number
        )
