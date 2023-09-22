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

    @property
    def properties_values(self):
        return [self.number, self.name]

    def __eq__(self, other):
        return self.properties_values == other.properties_values
