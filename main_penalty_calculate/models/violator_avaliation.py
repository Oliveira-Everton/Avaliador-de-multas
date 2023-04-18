class ViolatorAvaliation:
    def __init__(
        self,
        identity_card,
        license_plate,
        demerit_points,
        penalty_amount,
        status_driver_license
    ):
        self._identity_card = identity_card
        self._license_plate = license_plate
        self._demerit_points = demerit_points
        self._penalty_amount = penalty_amount
        self._status_driver_license = status_driver_license

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
    def demerit_points(self):
        return self._demerit_points

    @property
    def penalty_amount(self):
        return self._penalty_amount

    @property
    def status_driver_license(self):
        return self._status_driver_license
