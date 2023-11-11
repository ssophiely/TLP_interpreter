import grLexer
from Exceptions.Exceptions import NotAvailableError, VarError, Error


def id_check(id):
    if not id.lower().isalpha():
        raise VarError(id)
    if id in grLexer.KEY_WORDS:
        raise NotAvailableError(id)
    return


def number_check(num):
    if not num.isdigit():
        raise Error("число", num)
    return
