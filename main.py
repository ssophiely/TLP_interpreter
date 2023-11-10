import re

pat = re.compile(r"([:;+=/\-,()])")

# Разбиение входного файла на лексемы
with open("Program.txt") as file:
    lines = [pat.sub(" \\1 ", line.strip()) for line in file]
    lines_with_space = [" ".join(line.split()) for line in lines]
    tokens = sum([el.split(' ') for el in lines_with_space], [])

print(tokens)

# main = Tree(False, "main")
# t1 = Tree(True, "t1")
# main.add_children([t1])
# main.print_tree()

# Main = BuildMainTree()
# Main.print_root_left_right()
l = [1, 2, 3]
l = l[1:]
print(l)
