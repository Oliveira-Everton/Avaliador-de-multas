class IdentityCard:

    def __init__(self, id_number, id_name):
        self._id_number = id_number
        self._id_name = id_name

    @property
    def number(self):
        return self._id_number

    @property
    def name(self):
        return self._id_name
