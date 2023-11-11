from Tree_.Tree import Tree

lineBreak = Tree(True, ';')
colon = Tree(True, ':')
l_bracket = Tree(True, '(')
r_bracket = Tree(True, ')')
id = Tree(False, 'Id')
number = Tree(False, 'Number')
assign = Tree(True, '=')
unOp = Tree(False, "UnOp")


def build_main_tree():
    Program = Tree(False, "Prog")

    obPer = Tree(False, "ObPer")
    var = Tree(True, "var")
    type = Tree(True, 'integer')
    lPer = Tree(False, "LPer")
    obPer.add_children([var, lPer, colon, type, lineBreak])

    opVych = Tree(False, "OpVych")
    beg = Tree(True, 'begin')
    end = Tree(True, 'end')
    lPris = Tree(False, "LPris")
    pris = Tree(False, "Pris")
    lPris.add_children([pris])
    opVych.add_children([beg, lPris, end])

    Program.add_children([obPer, opVych])
    return Program


def build_in_tree():
    _read = Tree(True, "read")
    _in = Tree(False, "In")
    lPer = Tree(False, "LPer")
    _in.add_children([_read, l_bracket, lPer, r_bracket, lineBreak])
    return _in


def build_out_tree():
    _write = Tree(True, "write")
    _out = Tree(False, "Out")
    lPer = Tree(False, "LPer")
    _out.add_children([_write, l_bracket, lPer, r_bracket, lineBreak])
    return _out


def build_cond_tree():
    _case = Tree(True, "case")
    _of = Tree(True, "of")

    lVyb = Tree(False, "LVyb")
    lVyb.add_children([build_vyb_tree()])

    _end_case = Tree(True, "end_case")
    cond = Tree(False, "Cond")
    cond.add_children([_case, id, _of, lVyb, _end_case])
    return cond


def build_init_tree():
    init = Tree(False, "Init")
    vyr = Tree(False, "Vyr")
    init.add_children([id, assign, vyr, lineBreak])
    return init


def build_simple_expr_tree(op):
    simple = Tree(False, "Simple")
    pVyr1 = Tree(False, "PVyr1")
    simple.add_children([op, pVyr1])
    return simple


def build_complex_expr_tree():
    complex = Tree(False, "Init")
    vyr = Tree(False, "Vyr")
    pVyr1 = Tree(False, "PVyr1")
    complex.add_children([l_bracket, vyr, r_bracket, pVyr1])
    return complex


def build_minus_expr_tree():
    minExpr = Tree(False, "Init")
    pVyr = Tree(False, "PVyr")
    minExpr.add_children([unOp, pVyr])
    return minExpr


def build_vyb_tree():
    vyb = Tree(False, "Vyb")
    pris = Tree(False, "Pris")
    vyb.add_children([number, colon, pris])
    return vyb
