import globals as g
from Exceptions.Exceptions import *


def exe_trim():
    g.TOKENS_EXE = g.TOKENS_EXE[1:]


def find_ind(val):
    for ind, el in enumerate(g.TOKENS_EXE):
        if el[0] == val:
            return ind


# Начальная инициализация переменных
def vars_init():
    var_list = g.TOKENS_EXE[find_ind("var") + 1:find_ind(":")]

    for v in var_list:
        if v[0] != ',':
            g.VARS[v[0]] = 0

    g.TOKENS_EXE = g.TOKENS_EXE[find_ind(";") + 1:]


# Выполнение write
def write_exe():
    var_list = g.TOKENS_EXE[find_ind("(") + 1:find_ind(")")]

    for v in var_list:
        if v[0] != ',':
            print(g.VARS[v[0]], end='\t')
    print()

    g.TOKENS_EXE = g.TOKENS_EXE[find_ind(';') + 1:]


# Выполнение read
def read_exe():
    var_list = g.TOKENS_EXE[find_ind("(") + 1:find_ind(")")]

    for v in var_list:
        if v[0] != ',':
            g.VARS[v[0]] = int(input("Введите {0}\t".format(v[0])))

    g.TOKENS_EXE = g.TOKENS_EXE[find_ind(';') + 1:]


# Выполнение инициализации переменной
def init_exe():
    id = g.TOKENS_EXE[0]
    if id[0] not in g.VARS:
        raise NotDefinedError(id[0], id[1])
