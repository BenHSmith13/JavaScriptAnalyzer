import sys


def parse_file(f):
    with open(f, 'r') as in_file:
        for line_number, line in enumerate(in_file):
            for char_index, char in enumerate(line):
                print (line_number, char_index, char)


def main():
    # print "Hello World Mother F***er"
    parse_file(sys.argv[1])


if __name__ == "__main__":
    main()
