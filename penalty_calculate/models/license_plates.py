class LicensePlates:

    def __init__(self, license_plates=[]):
        self._license_plates = license_plates

    def check_plates(self):
        return self._license_plates

    def add_plate(self, plate):
        self._license_plates.append(plate)
