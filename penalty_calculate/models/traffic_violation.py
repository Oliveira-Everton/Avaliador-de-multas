from . import (
    IdentityCards,
    LicensePlates
)


class TrafficViolation:
    def __init__(
        self,
        identitycards=IdentityCards(),
        licenseplates=LicensePlates()
    ):
        self._identity_cards = identitycards
        self._license_plates = licenseplates
