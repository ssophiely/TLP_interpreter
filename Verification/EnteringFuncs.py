import globals
from Exceptions.Exceptions import SintaxError, EndError
from Verification.TermFuncs import *


def l_trim():
    globals.TOKENS = globals.TOKENS[1:]


def enter_LPer():
    x = globals.TOKENS[0]
    id_check(x)
    l_trim()
    if globals.TOKENS[0] == ',':
        l_trim()
        enter_LPer()
    return


def enter_Pris(node):
    import Tree_.TreeBuilding as b
    x = globals.TOKENS[0]
    if node.parent.value == "LPris":
        if x == "end":
            return

    if x == "read":
        node.add_children([b.build_in_tree()])
        return

    if x == "write":
        node.add_children([b.build_out_tree()])
        return

    if x == "case":
        node.add_children([b.build_cond_tree()])
        return

    node.add_children([b.build_init_tree()])


def enter_Vyr(node):
    from Tree_.Tree import Tree
    import Tree_.TreeBuilding as b
    x = globals.TOKENS[0]
    if x == '-':
        node.add_children([b.build_minus_expr_tree()])
        return

    pVyr = Tree(False, "PVyr")
    node.add_children([pVyr])


def enter_PVyr(node):
    import Tree_.TreeBuilding as b
    from Tree_.Tree import Tree
    x = globals.TOKENS[0]
    if x == '(':
        node.add_children([b.build_complex_expr_tree()])
        return

    if x.isalpha():
        node.add_children([b.build_simple_expr_tree(Tree(False, "Id"))])
        return

    if x.isdigit():
        node.add_children([b.build_simple_expr_tree(Tree(False, "Number"))])
        return

    if x.isalnum():
        raise VarError(x)

    raise SintaxError(x)


def enter_PVyr1(node):
    from Tree_.Tree import Tree
    x = globals.TOKENS[0]
    if x in grLexer.BIN_OP:
        binOp = Tree(False, "BinOp")
        pVyr = Tree(False, "PVyr")
        pVyr1 = Tree(False, "PVyr1")
        node.add_children([binOp, pVyr, pVyr1])

    return


def enter_Term(node):
    import Tree_.TreeBuilding as b
    t = globals.TOKENS[0]

    if t != node.value:
        raise Error(node.value, t)

    print(t, node.parent.value)
    if t == ';' and node.parent.value in ["Init", "In", "Out", "Cond"]:
        if node.parent.parent.parent.value == "LPris":
            l_trim()
            enter_Pris(node.parent.parent)
        else:
            l_trim()
            if globals.TOKENS[0] != "end_case":
                node.parent.parent.parent.parent.add_children([b.build_vyb_tree()])
        return

    l_trim()

    if t == "end" and len(globals.TOKENS) != 0:
        raise EndError()
