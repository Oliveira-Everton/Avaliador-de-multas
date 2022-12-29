from penalty_calculate.models.identity_card import IdentityCard
from penalty_calculate.models.license_plate import LicensePlate


class TrafficViolation:

    def __init__(
        self,
        model_id_card=IdentityCard(),
        model_license_plate=LicensePlate()
    ):
        self._id_card = model_id_card
        self._license_plate = model_license_plate

    @property
    def id_card(self):
        return self._id_card

    @property
    def license_plate(self):
        return self._license_plate
