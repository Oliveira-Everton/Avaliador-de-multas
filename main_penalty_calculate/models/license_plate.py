class LicensePlate:
    def __init__(self, number, type_infraction):
        self._number = number
        self._type_infraction = type_infraction

    @property
    def number(self):
        return self._number

    @property
    def type_infraction(self):
        return self._type_infraction
