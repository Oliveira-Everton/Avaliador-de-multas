from .parsers.file_parser import FileParser


class PenaltyCalculate:

    def __init__(self, csv_file):
        self._csv_file = csv_file

    def csv_reader(self):
        return FileParser(
            self._csv_file
        ).take_id_cards_with_license_plate()

        # O retorno dele vai ser o output_serializer e não o file_parser

    # Essa função não retornar o file parser
    # pq o file parser não tem que retornar essas coisas...
    # Ele apenas lê o arquivo e joga tudo num modelo de dados...
    # Então essa função ainda vai chamar o
    # fileparser mas o retorno dela vai ser outro queridão
