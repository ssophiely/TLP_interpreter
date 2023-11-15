from Verification.EnteringFuncs import *


class Tree:
    def __init__(self, term, value):
        self.term = term
        self.value = value
        self.children = []
        self.parent = None

    def add_children(self, list):
        self.children += list
        for child in list:
            child.parent = self

    def check_root_left_right(self):
        if self is None:
            return

        # print(self.value)
        self.current_node()
        for child in self.children:
            child.check_root_left_right()

    def current_node(self):
        t = globals.TOKENS[0]

        if self.term:
            enter_Term(self)

        elif self.value == "LPer":
            enter_LPer()

        elif self.value == "Pris":
            enter_Pris(self)

        elif self.value == "Id":
            id_check(t[0], t[1])
            l_trim()
            return

        elif self.value == "Vyr":
            enter_Vyr(self)

        elif self.value == "UnOp":
            l_trim()
            return

        elif self.value == "BinOp":
            l_trim()
            return

        elif self.value == "Number":
            number_check(t[0], t[1])
            l_trim()
            return

        elif self.value == "PVyr":
            enter_PVyr(self)

        elif self.value == "PVyr1":
            enter_PVyr1(self)

        else:
            return
