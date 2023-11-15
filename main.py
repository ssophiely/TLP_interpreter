import re

import globals
from Tree_.TreeBuilding import *

pat = re.compile(r"([:;+=/\-,()])")

# Разбиение входного файла на лексемы
with open("Program1.txt") as file:
    lines = [pat.sub(" \\1 ", line.strip()) for line in file]
    lines_with_space = [" ".join(line.split()) for line in lines]
    globals.TOKENS = [[x, ind + 1] for ind, el in enumerate(lines_with_space) for x in el.split(' ')]

print(globals.TOKENS)

Main = build_main_tree()
Main.check_root_left_right()
