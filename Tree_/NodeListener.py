from Verification.EnteringFuncs import *
from Verification.TermFuncs import *


def current_node(node):
    t = main.TOKENS[0]

    if node.term:
        if t != node.value:
            raise Error(node.value, t)

        if t in [';', "end_case"] and node.parent.value in ["Init", "In", "Out", "Cond"]:
            if node.parent.parent.parent.value == "LPris":
                l_trim()
                enter_Pris(node.parent.parent)
            else:
                l_trim()
                if main.TOKENS[0] != "end_case":
                    node.parent.parent.parent.parent.add_children([build_vyb_tree()])
        else:
            l_trim()

        return

    elif node.value == "LPer":
        enter_LPer()

    elif node.value == "Pris":
        enter_Pris()

    elif node.value == "Id":
        id_check(t)
        l_trim()
        return

    elif node.value == "Vyr":
        enter_Vyr(node)

    elif node.value == "UnOp":
        l_trim()
        return

    elif node.value == "BinOp":
        l_trim()
        return

    elif node.value == "Number":
        number_check(t)
        l_trim()
        return

    elif node.value == "PVyr":
        enter_PVyr(node)

    elif node.value == "PVyr1":
        enter_PVyr1(node)

    else:
        return
