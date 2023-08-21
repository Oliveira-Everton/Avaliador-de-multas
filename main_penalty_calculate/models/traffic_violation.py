class TrafficViolation:
    def __init__(
        self,
        identity_card,
        license_plate,
        type_infraction,
        infraction_date,
        notification_date
    ):
        self._identity_card = identity_card
        self._license_plate = license_plate
        self._type_infraction = type_infraction
        self._infraction_date = infraction_date
        self._notification_date = notification_date

    @property
    def identity_card(self):
        return self._identity_card

    @property
    def license_plate(self):
        return self._license_plate

    @property
    def type_infraction(self):
        return self._type_infraction

    @property
    def infraction_date(self):
        return self._infraction_date

    @property
    def notification_date(self):
        return self._notification_date

    def _properties_values(self):
        return [
            self.identity_card,
            self.license_plate,
            self.type_infraction,
            self.infraction_date,
            self.notification_date
        ]

    def __eq__(self, other):
        return self._properties_values() == other._properties_values()
