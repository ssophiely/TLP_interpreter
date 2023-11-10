class Error(Exception):
    def __init__(self, *args):
        self.expect = args[0]
        self.found = args[1]

    def __str__(self):
        return 'Ожидалось {0}, найдено {1}.'.format(self.expect, self.found)


class VarError(Exception):
    def __init__(self, *args):
        self.var = args[0]

    def __str__(self):
        return 'Переменная {0} содержит недопустимые символы.'.format(self.var)
