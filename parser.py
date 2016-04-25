# Aaron Light - A01185262
# Ben Smith - A01208763
# Joseph Ditton - A01249280
# Seth Bertlshofer - A00933231

separators = [" ", "\n", "(", ")", "{", "}", ".", ",", ":", "[", "]", ";", "=", "!", "+", "-", "/", "*"]


# separate all chars
def parse_file(f):
    lexemes = []
    with open(f, 'r') as in_file:
        for line_number, line in enumerate(in_file):
            for char_index, char in enumerate(line):
                lexemes.append((line_number, char_index, char))
    return lexemes


# takes chars and builds them into "words" defined by a list of separators
def build_words(chars):
    words = []
    word = ""
    open_quote = "" #need to keep track of open and closed quotes
    for char in chars:
        # control the state of whether we are looking at a string literal or not.
        if char[2] in "\"'" and char[2] != open_quote:
            open_quote = char[2]
        elif char[2] == open_quote:
            open_quote = ""
        if char[2] in separators:
            # if we are inside of a string then treat everything as part of the word.
            if open_quote != "":
                word += char[2]
            #if we have found break and we are not in a string then add that word to the list.
            elif word and open_quote == "":
                words.append((word, char[0]))  # add the word and the line number.
                word = ""
            #if we have found a break but dont have a word then add the break char to the list.
            elif not word and open_quote == "":
                words.append((char[2], char[0]))
        else:
            word += char[2]
    return words

# Aaron Light - A01185262
# Ben Smith - A01208763
# Joseph Ditton - A01249280
# Seth Bertlshofer - A00933231
