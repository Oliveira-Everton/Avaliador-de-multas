class TypeInfraction:
    def __init__(self, type_infraction):
        self._type_infraction = type_infraction

    @property
    def type(self):
        return self._type_infraction
