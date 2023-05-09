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
