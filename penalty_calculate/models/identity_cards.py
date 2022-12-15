class IdentityCards:

    def __init__(self, identity_numbers=[], identity_names=[]):
        self._numbers = identity_numbers
        self._names = identity_names

    def check_numbers(self):
        return self._numbers

    def check_names(self):
        return self._names

    def add_name(self, name):
        self._names.append(name)

    def add_number(self, number):
        self._numbers.append(number)
