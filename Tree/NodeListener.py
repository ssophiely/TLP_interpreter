from Exceptions.Exceptions import Error
from Funcs import *


def current_node(node):
    if node.term:
        if main.tokens[0] != node.value:
            raise Error(node.value, main.tokens[0])
        main.tokens = main.tokens[1:]
        return

    if node.value == "LPer":
        EnterLPer()
