from Tree.Tree import Tree

lineBreak = Tree(True, ';')
colon = Tree(True, ':')
l_bracket = Tree(True, '(')
r_bracket = Tree(True, ')')
id = Tree(False, 'Id')
number = Tree(False, 'Number')
assign = Tree(True, '=')
binOp = Tree(False, "BinOp")
unOp = Tree(False, "UnOp")


def BuildMainTree():
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
    opVych.add_children([beg, lPris, end])

    Program.add_children([obPer, opVych])
    return Program


def BuildInTree():
    _read = Tree(True, "read")
    _in = Tree(False, "In")
    lPer = Tree(False, "LPer")
    _in.add_children([_read, l_bracket, lPer, r_bracket, lineBreak])
    return _in


def BuildOutTree():
    _write = Tree(True, "write")
    _out = Tree(False, "Out")
    lPer = Tree(False, "LPer")
    _out.add_children([_write, l_bracket, lPer, r_bracket, lineBreak])
    return _out


def BuildCondTree():
    _case = Tree(True, "case")
    _of = Tree(True, "of")

    lVyb = Tree(False, "LVyb")
    vyb = Tree(False, "Vyb")
    pris = Tree(False, "Pris")
    vyb.add_children([number, colon, pris])
    lVyb.add_children([vyb])

    _end_case = Tree(True, "end_case")
    cond = Tree(False, "Cond")
    cond.add_children([_case, id, _of, lVyb, _end_case])
    return cond


def BuildInitTree():
    init = Tree(False, "Init")
    vyr = Tree(False, "Vyr")
    init.add_children([id, assign, vyr, lineBreak])
    return init


def BuildSimpleExprTree():
    simple = Tree(False, "Simple")
    op = Tree(False, "Op")
    pVyr1 = Tree(False, "PVyr1")
    simple.add_children([op, pVyr1])
    return simple


def BuildComplexExprTree():
    complex = Tree(False, "Init")
    vyr = Tree(False, "Vyr")
    pVyr1 = Tree(False, "PVyr1")
    complex.add_children([l_bracket, vyr, r_bracket, pVyr1])
    return complex


def BuildMinusExprTree():
    minExpr = Tree(False, "Init")
    pVyr = Tree(False, "PVyr")
    minExpr.add_children([unOp, pVyr])
    return minExpr
