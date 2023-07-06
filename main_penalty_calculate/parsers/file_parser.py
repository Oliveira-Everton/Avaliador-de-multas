import csv


class FileParser:
    _READ_PARAMETER = 'r'
    _DELIMITER = ';'
    _UNICODE = 'utf-8'

    def __init__(self, file_name):
        self._file_name = file_name

    def convert_file(self):
        with open(
            self._file_name,
            mode=self._READ_PARAMETER,
            encoding=self._UNICODE
        ) as file:
            reader_csv = csv.reader(file, delimiter=self._DELIMITER)
            return list(enumerate(reader_csv))
