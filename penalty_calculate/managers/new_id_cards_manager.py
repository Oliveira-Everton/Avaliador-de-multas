class NewIdCardsManager:
    def __init__(self, id_cards_models=[]):
        self._identity_cards = id_cards_models

    def _analyze_models(self):
        for index, model in enumerate(self._identity_cards):
            print(index, model.name, model.number)
# consegui varrer os modelos de dados...Segue daqui!
