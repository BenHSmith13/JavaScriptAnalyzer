#!/usr/bin/python2.7

# Aaron Light - A01185262
# Ben Smith - A01208763
# Joseph Ditton - A01249280
# Seth Bertlshofer - A00933231

import sys

import parser
import tokenizer
import syntaxer  # Sytaxer, I hardly know her


def main():
    if len(sys.argv) > 1:
        lexemes = parser.parse_file(sys.argv[1])
        words = parser.build_words(lexemes)
        tokens = tokenizer.tokenize(words)
        for token in tokens:
            print((token[0], token[1]))
        syntaxer.analyze(tokens)
    else:
        print('Error: missing parameter\n\t- please specify a file')


if __name__ == "__main__":
    main()

# Aaron Light - A01185262
# Ben Smith - A01208763
# Joseph Ditton - A01249280
# Seth Bertlshofer - A00933231
