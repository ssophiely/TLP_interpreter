import string

# Терминальный словарь
BinOp = ['+', '-', '/']
UnOp = ["-"]
Letter = list(string.ascii_uppercase) + list(string.ascii_lowercase)
Number = [i for i in range(0, 10)]
SpecialOp = [';', ':', '=', ',', '(', ')']
KeyWords = ["var", "begin", "integer", "write", "read", "case", "of", "end_case"]
