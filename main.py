import re

from SintaxTree.TreeBuilding import *

pat = re.compile(r"([:;+=/\-,()])")

# Разбиение входного файла на лексемы
with open("Program1.txt") as file:
    lines = [pat.sub(" \\1 ", line.strip()) for line in file]
    lines_with_space = [" ".join(line.split()) for line in lines]
    g.TOKENS = [[x, ind + 1] for ind, el in enumerate(lines_with_space) for x in el.split(' ')]

Main = build_main_tree()
Main.parse()

print("Идентификаторы:\t", list(g.VARS.keys()))
print("Зарезервированные слова:\t", list(grLexer.KEY_WORDS_OUT))
print("Специальные операторы:\t", list(grLexer.SPECIAL_OP_OUT))
print("Бинарные операторы:\t", list(grLexer.BIN_OP_OUT))
print("Унарные операторы:\t", list(grLexer.UN_OP_OUT))

Main.execute()
