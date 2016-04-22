#!/usr/bin/python3

# Aaron Light
# Ben Smith
# Joseph Ditton
# Seth Bertlshofer - A00933231

import sys

import parser
import tokenizer


def main():
    if len(sys.argv) > 1:
        lexemes = parser.parse_file(sys.argv[1])
        words = parser.build_words(lexemes)
        tokens = tokenizer.tokenize(words)
        print tokens
    else:
        print('Error: missing parameter\n\t- please specify a file')


if __name__ == "__main__":
    main()

# Aaron Light
# Ben Smith
# Joseph Ditton
# Seth Bertlshofer - A00933231
