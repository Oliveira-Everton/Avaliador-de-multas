class IdCardsManager:
    def __init__(self, identity_cards):
        self._identity_card = identity_cards

    def _id_numbers(self):
        return self._identity_card.check_numbers()

    def _id_names(self):
        return self._identity_card.check_names()

    def _align_id_cards(self):
        align_id = []
        for line_numbers, column_numbers in enumerate(self._id_numbers()):
            for line_names, column_names in enumerate(self._id_names()):
                if line_numbers == line_names:
                    dictionary = {column_numbers: column_names}
                    align_id.append(dictionary.copy())
        return align_id

    def take_id_cards(self):
        return self._align_id_cards()
