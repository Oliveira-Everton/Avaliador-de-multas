from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.license_plate import LicensePlate


class TrafficViolation:

    def __init__(
        self,
        id_card=IdentityCard(),
        license_plate=LicensePlate()
    ):
        self._id_card = id_card
        self._license_plate = license_plate

    @property
    def id_card(self):
        return self._id_card

    @property
    def license_plate(self):
        return self._license_plate
