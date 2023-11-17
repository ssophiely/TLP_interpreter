class Error(Exception):
    def __init__(self, *args):
        self.expect = args[0]
        self.found = args[1]
        self.str = args[2]

    def __str__(self):
        return 'Ожидалось {0}, найдено {1}. Строка {2}.'.format(self.expect, self.found, self.str)


class VarError(Exception):
    def __init__(self, *args):
        self.var = args[0]
        self.str = args[1]

    def __str__(self):
        return 'Переменная {0} содержит недопустимые символы. Строка {1}.'.format(self.var, self.str)


class LengthError(Exception):
    def __init__(self, *args):
        self.var = args[0]
        self.str = args[1]

    def __str__(self):
        return 'Длина переменной {0} не должна превышать 11. Строка {1}.'.format(self.var, self.str)


class NotAvailableError(Exception):
    def __init__(self, *args):
        self.var = args[0]
        self.str = args[1]

    def __str__(self):
        return 'Имя {0} зарезервировано. Строка {1}.'.format(self.var, self.str)


class SintaxError(Exception):
    def __init__(self, *args):
        self.var = args[0]
        self.str = args[1]

    def __str__(self):
        return 'Синтаксичсекая ошибка: {0}. Строка {1}.'.format(self.var, self.str)


class EndError(Exception):
    def __init__(self, *args):
        self.str = args[0]

    def __str__(self):
        return 'Недопустимые символы после end. Строка {0}.'.format(self.str)


class BeenDefinedError(Exception):
    def __init__(self, *args):
        self.var = args[0]
        self.str = args[1]

    def __str__(self):
        return 'Переменная {0} уже определена. Строка {1}.'.format(self.var, self.str)


class NotDefinedError(Exception):
    def __init__(self, *args):
        self.var = args[0]
        self.str = args[1]

    def __str__(self):
        return 'Переменная {0} не определена. Строка {1}.'.format(self.var, self.str)


class NotInitError(Exception):
    def __init__(self, *args):
        self.var = args[0]
        self.str = args[1]

    def __str__(self):
        return 'Переменной {0} не присвоено значение. Строка {1}.'.format(self.var, self.str)


class CondNumError(Exception):
    def __init__(self, *args):
        self.var = args[0]
        self.str = args[1]

    def __str__(self):
        return 'Значение {0} должно быть уникальным. Строка {1}.'.format(self.var, self.str)


class CondVarError(Exception):
    def __init__(self, *args):
        self.var = args[0]
        self.str = args[1]

    def __str__(self):
        return 'Во вложенных блоках case...of найдены одинаковые переменные {0}. Строка {1}.'.format(self.var, self.str)
