import string

# Терминальный словарь
BIN_OP = ['+', '-', '/']
UN_OP = ["-"]
LETTER = list(string.ascii_uppercase) + list(string.ascii_lowercase)
NUMBER = [i for i in range(0, 10)]
SPECIAL_OP = [';', ':', '=', ',', '(', ')']
KEY_WORDS = ["var", "begin", "integer", "write", "read", "case", "of", "end_case", "end"]

# Терминальный словарь для вывода
BIN_OP_OUT = set()
UN_OP_OUT = set()
SPECIAL_OP_OUT = set()
KEY_WORDS_OUT = set()
