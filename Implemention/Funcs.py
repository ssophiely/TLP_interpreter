import globals as g


# Выполнение write или read
def lPer_exe(node):
    if node.parent.value == "ObPer":
        return

    if node.parent.value == "Out":
        for v in node.val:
            print(g.VARS[v], end='\t')
        print()
        return

    if node.parent.value == "In":
        for v in node.val:
            g.VARS[v] = int(input("Введите {0}\t".format(v)))
        return


# Выполнение присваивания значения переменной
def init_exe(vyr):
    id = vyr.parent.children[0].val
    l = []
    create_vyr(vyr, l)
    g.VARS[id] = eval(''.join(l))


def create_vyr(node, l):
    if node is None:
        return

    if node.value in ["UnOp", "BinOp", "Number"]:
        l += [str(node.val)]
    if node.value == "Id":
        l += [str(g.VARS[node.val])]
    if node.term:
        l += [node.val]

    for child in node.children:
        create_vyr(child, l)
