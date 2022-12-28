class LicensePlate:

    def __init__(self, plate_car):
        self._plate_car = plate_car

    @property
    def number(self):
        return self._plate_car
