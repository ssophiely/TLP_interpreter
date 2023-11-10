import main
from Exceptions.Exceptions import VarError


def EnterLPer():
    x = main.tokens[0]
    if not x.lower().isalpha():
        raise VarError(x)
