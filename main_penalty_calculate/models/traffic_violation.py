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
    def identity_card_number(self):
        return self._identity_card.number

    @property
    def identity_card_name(self):
        return self._identity_card.name

    @property
    def license_plate_number(self):
        return self._license_plate.number

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
            self.identity_card_number,
            self.identity_card_name,
            self.license_plate_number,
            self.type_infraction.type,
            self.infraction_date,
            self.notification_date
        ]

    def __eq__(self, other):
        return self._properties_values() == other._properties_values()
