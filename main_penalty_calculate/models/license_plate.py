class LicensePlate:
    def __init__(self, number):
        self._number = number

    @property
    def number(self):
        return self._number

    def __eq__(self, other):
        return self.number == other.number
