#!/usr/bin/python2.7

# Aaron Light
# Ben Smith
# Joseph Ditton
# Seth Bertlshofer - A00933231

import sys

import parser
import tokenizer
import syntaxer  # Sytaxer, I hardly know her


def main():
    if len(sys.argv) > 1:
        lexemes = parser.parse_file(sys.argv[1])
        words = parser.build_words(lexemes)
        print words
        tokens = tokenizer.tokenize(words)
        for token in tokens
            print(tokens)
        syntaxer.analyze(tokens)
    else:
        print('Error: missing parameter\n\t- please specify a file')


if __name__ == "__main__":
    main()

# Aaron Light
# Ben Smith
# Joseph Ditton
# Seth Bertlshofer - A00933231
