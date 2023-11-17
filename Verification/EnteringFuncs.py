import globals
from Exceptions.Exceptions import *
from Verification.TermFuncs import *


def l_trim():
    globals.TOKENS = globals.TOKENS[1:]


def enter_LPer(node):
    x = globals.TOKENS[0]
    id_check(x[0], x[1])

    if node.parent.value == "ObPer":
        if x[0] not in globals.VARS:
            globals.VARS[x[0]] = 0
        else:
            raise BeenDefinedError(x[0], x[1])

    if node.parent.value in ["Out", "In"]:
        if x[0] not in globals.VARS:
            raise NotDefinedError(x[0], x[1])

        if node.parent.value == "Out":
            if x[0] not in globals.VARS_INIT:
                raise NotInitError(x[0], x[1])
        if node.parent.value == "In":
            globals.VARS_INIT.add(x[0])

    l_trim()
    if globals.TOKENS[0][0] == ',':
        l_trim()
        enter_LPer(node)
    return


def enter_Pris(node):
    import Tree_.TreeBuilding as b
    x = globals.TOKENS[0][0]
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
    x = globals.TOKENS[0][0]
    if x == '-':
        node.add_children([b.build_minus_expr_tree()])
        return

    pVyr = Tree(False, "PVyr")
    node.add_children([pVyr])


def enter_PVyr(node):
    import Tree_.TreeBuilding as b
    from Tree_.Tree import Tree
    x = globals.TOKENS[0][0]
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

    raise SintaxError(x, globals.TOKENS[0][1])


def enter_PVyr1(node):
    from Tree_.Tree import Tree
    x = globals.TOKENS[0][0]
    if x in grLexer.BIN_OP:
        binOp = Tree(False, "BinOp")
        pVyr = Tree(False, "PVyr")
        pVyr1 = Tree(False, "PVyr1")
        node.add_children([binOp, pVyr, pVyr1])

    return


def enter_Term(node):
    import Tree_.TreeBuilding as b
    t = globals.TOKENS[0][0]

    if t != node.value:
        raise Error(node.value, t, globals.TOKENS[0][1])

    # Добавления терминала в соответсвующий список для лексического анализа
    if t in grLexer.KEY_WORDS:
        grLexer.KEY_WORDS_OUT.add(t)
    if t in grLexer.SPECIAL_OP:
        grLexer.SPECIAL_OP_OUT.add(t)

    if t == ';' and node.parent.value in ["Init", "In", "Out", "Cond"]:
        if node.parent.value == "Init":
            globals.VARS_INIT.add(globals.VARS_INIT.add(globals.INIT))

        if node.parent.parent.parent.value == "LPris":
            l_trim()
            enter_Pris(node.parent.parent)
        else:
            l_trim()
            if globals.TOKENS[0][0] != "end_case":
                node.parent.parent.parent.parent.add_children([b.build_vyb_tree()])
        return

    l_trim()

    if t == "end" and len(globals.TOKENS) != 0:
        raise EndError(globals.TOKENS[0][1])
