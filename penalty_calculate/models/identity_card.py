class IdentityCard:

    def __init__(self, id_number='', id_name=''):
        self._number = id_number
        self._name = id_name

    @property
    def number(self):
        return self._number

    @property
    def name(self):
        return self._name
