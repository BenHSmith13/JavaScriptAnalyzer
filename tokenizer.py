keywords = ["var", "function", "if", "else", "break", "switch", "case", "return"]


# assign each word a part of grammer
def tokenize(words):
    tokens = []
    for word_tup in words:
        word = word_tup[0]
        if word in keywords:
            tokens.append(("KEYWORD", word, word_tup[1]))
        elif word in [" ", "\t"]:
            tokens.append(("WHITESPACE", word, word_tup[1]))
        elif word in [";", "\n"]:
            tokens.append(("DELIMITER", word, word_tup[1]))
        elif word == "(":
            tokens.append(("OPEN_PARAM", word, word_tup[1]))
        elif word == ")":
            tokens.append(("CLOSE_PARAM", word, word_tup[1]))
        elif word == "{":
            tokens.append(("OPEN_BLOCK", word, word_tup[1]))
        elif word == "}":
            tokens.append(("CLOSE_BLOCK", word, word_tup[1]))
        elif word == "[":
            tokens.append(("OPEN_SUBSCRIPT", word, word_tup[1]))
        elif word == "]":
            tokens.append(("CLOSE_SUBSCRIPT", word, word_tup[1]))
        elif word in "=!+-/*.":
            tokens.append(("OPERATOR", word, word_tup[1]))
        else:
            refined_token = refiner_and_lexical_error_parser(("IDENT", word, word_tup[1]))
            tokens.append(refined_token)
    return tokens


# separate the literals and the identifiers: Built to handle strings, ints, boolean primitive types
def refiner_and_lexical_error_parser(token):
    num_chars = "0123456789"
    word = token[1]
    # only get the IDENT types, the others are what they are because their word matches something exactly already
    if token[0] == "IDENT":
        # handle strings
        if "\"" in word or "'" in word:
            if (word[0] == "\"" and word[-1] == "\"") or (word[0] == "'" and word[-1] == ""):
                return "STR_LITERAL", word, token[2]
            else:
                raise LexicalError("Lexical error at line: " + str(token[2]) + ", invalid string literal: " + word)
        # handle numbers, TODO: figure our floating point
        elif word[0] in num_chars:
            check_valid_number(word, token[2])
            return "INT_LITERAL", word, token[2]
        # handle booleans
        elif word == "true" or word == "false":
            return "BOOL_LITERAL", word, token[2]
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
