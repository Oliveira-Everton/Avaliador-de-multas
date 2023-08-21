class IdentityCard:
    def __init__(self, number, name):
        self._number = number
        self._name = name

    @property
    def number(self):
        return self._number

    @property
    def name(self):
        return self._name

    def _properties_values(self):
        [self.name, self.number]

    def __eq__(self, other):
        return self._properties_values() == other._properties_values()
