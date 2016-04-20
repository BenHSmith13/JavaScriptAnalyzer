#!/usr/bin/python3

# Aaron Light
# Ben Smith
# Joseph Ditton
# Seth Bertlshofer - A00933231

import sys

def parse_file(f):
    with open(f, 'r') as in_file:
        for line_number, line in enumerate(in_file):
            for char_index, char in enumerate(line):
                print (line_number, char_index, char)

def main():
    # print "Hello World Mother F***er"
    if len(sys.argv) > 1:
        parse_file(sys.argv[1])
    else:
        print('Error: missing parameter\n\t- please specify a file')

if __name__ == "__main__":
    main()

# Aaron Light
# Ben Smith
# Joseph Ditton
# Seth Bertlshofer - A00933231
