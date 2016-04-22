keywords = [
    "var",
    "function",
    "if",
    "else",
    "break",
    "switch",
    "case",
    "return",
    "while",
    "for",
    "let",
    "then",
    "this",
    "catch"
    ]


# assign each word a part of grammer
def tokenize(words):
    tokens = []
    for word_tup in words:
        word = word_tup[0]
        if word in keywords:
            tokens.append(("KEYWORD", word, word_tup[1]))
        elif word in [";", "\n"]:
            tokens.append(("END_MARKER", word, word_tup[1]))
        elif word in "()\{\}[]=!+-/*.":
            tokens.append(("PUNCT", word, word_tup[1]))
        elif word not in [" ", "\t", "\v" "\f"]:
            refined_token = refiner_and_lexical_error_parser(("ID", word, word_tup[1]))
            tokens.append(refined_token)
    return tokens


# separate the literals and the identifiers: Built to handle strings, ints, boolean primitive types
def refiner_and_lexical_error_parser(token):
    num_chars = "0123456789"
    word = token[1]
    # only get the IDENT types, the others are what they are because their word matches something exactly already
    if token[0] == "ID":
        # handle strings
        if "\"" in word or "'" in word:
            if (word[0] == "\"" and word[-1] == "\"") or (word[0] == "'" and word[-1] == "'"):
                return "LIT", word, token[2]
            else:
                raise LexicalError("Lexical error at line: " + str(token[2]) + ", invalid string literal: " + word)
        # handle numbers, TODO: figure our floating point
        elif word[0] in num_chars:
            check_valid_number(word, token[2])
            return "LIT", word, token[2]
        # handle booleans
        elif word == "true" or word == "false":
            return "LIT", word, token[2]
        # put everything else back the way it was because
        else:
            return token
    else:
        return token
    #  This return in unreachable
    return refined_tokens


def check_valid_number(num, line):
    invalid_chars = "qwertyiop[]\\\{\}|asdfghjkl;:'\"zxcvbn,./<>?!@#$%^&*()-_=+"
    for digit in num:
        if digit in invalid_chars:
            raise LexicalError("Lexical error at line: " + str(line) + ", invalid character in number: " + num)


class LexicalError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
