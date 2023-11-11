import re

from Tree_.TreeBuilding import *

pat = re.compile(r"([:;+=/\-,()])")

# Разбиение входного файла на лексемы
with open("Program.txt") as file:
    lines = [pat.sub(" \\1 ", line.strip()) for line in file]
    lines_with_space = [" ".join(line.split()) for line in lines]
    TOKENS = sum([el.split(' ') for el in lines_with_space], [])

print(TOKENS)

Main = build_main_tree()
# Main.check_root_left_right()
