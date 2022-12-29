class TrafficViolation:

    def __init__(self, models_id_cards=[], license_plates=[]):
        self._models_id_cards = models_id_cards
        self._license_plates = license_plates

    @property
    def id_cards(self):
        return self._models_id_cards

    @property
    def license_plates(self):
        return self._license_plates
