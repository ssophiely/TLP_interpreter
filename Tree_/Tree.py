from Implemention.Funcs import *
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

    # Синтаксический анализ программы
    def check_root_left_right(self):
        if self is None:
            return

        self.current_node()
        
        for child in self.children:
            child.check_root_left_right()

    def current_node(self):
        t = globals.TOKENS[0]

        if self.term:
            enter_Term(self)

        elif self.value == "LPer":
            enter_LPer(self)

        elif self.value == "Pris":
            enter_Pris(self)

        elif self.value == "Id":
            id_check(t[0], t[1])

            # проверка переменной на определение
            not_def_error(t[0], t[1])

            if self.parent.value == "Init":
                globals.INIT = t[0]

            # проверка переменной на инициализацию
            if self.parent.value == "Cond" or self.parent.value == "Simple":
                not_init_error(t[0], t[1])

            l_trim()
            return

        elif self.value == "Vyr":
            enter_Vyr(self)

        elif self.value == "UnOp":
            grLexer.UN_OP_OUT.add(t[0])
            l_trim()
            return

        elif self.value == "BinOp":
            grLexer.BIN_OP_OUT.add(t[0])
            l_trim()
            return

        elif self.value == "Number":
            number_check(t[0], t[1])

            # проверка на уникальность значений в case
            if self.parent.value == "Vyb":
                l_nums = self.parent.parent.parent.nums
                if t[0] in l_nums:
                    raise CondNumError(t[0], t[1])
                l_nums += [t[0]]

            l_trim()
            return

        elif self.value == "PVyr":
            enter_PVyr(self)

        elif self.value == "PVyr1":
            enter_PVyr1(self)

        else:
            return

    # Выполнение программы
    def execute_root_left_right(self):
        if self is None:
            return

        self.current_node_exe()
        for child in self.children:
            child.execute_root_left_right()

    def current_node_exe(self):
        if self.value == "ObPer":
            vars_init()
            self.children = []
            return

        if self.value == "Out":
            write_exe()
            self.children = []
            return

        if self.value == "In":
            read_exe()
            self.children = []
            return

        if self.value == "Init":
            init_exe()
            self.children = []
            return
