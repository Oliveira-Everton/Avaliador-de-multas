class TrafficViolation:

    def __init__(self, models_id=[], license_plates=[]):
        self._models_id = models_id
        self._license_plates = license_plates

    @property
    def id_cards(self):
        return self._models_id

    @property
    def license_plates(self):
        return self._license_plates
