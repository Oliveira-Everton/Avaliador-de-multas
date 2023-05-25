class ViolatorAvaliation:
    def __init__(
        self,
        identity_card,
        license_plates
    ):
        self._identity_card = identity_card
        self._license_plates = license_plates

    @property
    def identity_card_number(self):
        return self._identity_card.number

    @property
    def identity_card_name(self):
        return self._identity_card.name

    @property
    def license_plate_numbers(self):
        return self._license_plates.numbers

    def _compare_properties(self, violator_avaliation):
        return [
            violator_avaliation.identity_card_number,
            violator_avaliation.identity_card_name,
            violator_avaliation.license_plate_numbers
        ]

    def __eq__(self, other):
        return (
            self._compare_properties(self) == self._compare_properties(other)
        )
