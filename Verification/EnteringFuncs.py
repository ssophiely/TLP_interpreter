import main
from Exceptions.Exceptions import SintaxError
from Verification.TermFuncs import *
from Tree_.TreeBuilding import *


def l_trim():
    main.TOKENS = main.TOKENS[1:]


def enter_LPer():
    x = main.TOKENS[0]
    id_check(x)
    l_trim()
    if main.TOKENS[0] == ',':
        l_trim()
        enter_LPer()
    return


def enter_Pris(node):
    x = main.TOKENS[0]

    if node.parent.value == "LPris":
        if x == "end":
            return

    if x == "read":
        node.add_children([build_in_tree(), ])
        return

    if x == "write":
        node.add_children([build_out_tree()])
        return

    if x == "case":
        node.add_children([build_cond_tree()])
        return

    node.add_children([build_init_tree()])


def enter_Vyr(node):
    x = main.TOKENS[0]
    if x == '-':
        node.add_children([build_minus_expr_tree()])
        return

    pVyr = Tree(False, "PVyr")
    node.add_children([pVyr])


def enter_PVyr(node):
    x = main.TOKENS[0]
    if x == '(':
        node.add_children([build_complex_expr_tree()])
        return

    if x.isalpha():
        node.add_children([build_simple_expr_tree(Tree(False, "Id"))])
        return

    if x.isdigit():
        node.add_children([build_simple_expr_tree(Tree(False, "Number"))])
        return

    if x.isalnum():
        raise VarError(x)

    raise SintaxError(x)


def enter_PVyr1(node):
    x = main.TOKENS[0]
    if x in grLexer.BIN_OP:
        binOp = Tree(False, "BinOp")
        pVyr = Tree(False, "PVyr")
        pVyr1 = Tree(False, "PVyr1")
        node.add_children([binOp, pVyr, pVyr1])

    return
