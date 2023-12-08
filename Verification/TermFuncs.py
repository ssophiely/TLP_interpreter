import grLexer
from Exceptions.Exceptions import *


def id_check(id, str):
    if not id.lower().isalpha():
        raise VarError(id, str)
    if id in grLexer.KEY_WORDS:
        raise NotAvailableError(id, str)
    if len(id) > 11:
        raise LengthError(id, str)
    return


def number_check(num, str):
    if not num.isdigit():
        raise Error("число", num, str)
    return
