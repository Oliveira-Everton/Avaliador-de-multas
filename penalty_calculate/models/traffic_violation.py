from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.license_plate import LicensePlate


class TrafficViolation:

    def __init__(
        self,
        identity_card=IdentityCard(),
        license_plate=LicensePlate()
    ):
        self._identity_card = identity_card
        self._license_plate = license_plate

    @property
    def identity_card(self):
        return self._identity_card

    @property
    def license_plate(self):
        return self._license_plate
