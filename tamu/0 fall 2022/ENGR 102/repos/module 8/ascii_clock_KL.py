# creates a dictionary to translate from user inputed text to individual lines to print
# each cell describes one character from top to bottom as the array indicies increase
translate = {
    "0": ["000 ", "0 0 ", "0 0 ", "0 0 ", "000 "],
    "1": [" 1  ", "11  ", " 1  ", " 1  ", "111 "],
    "2": ["222 ", "  2 ", "222 ", "2   ", "222 "],
    "3": ["333 ", "  3 ", "333 ", "  3 ", "333 "],
    "4": ["4 4 ", "4 4 ", "444 ", "  4 ", "  4 "],
    "5": ["555 ", "5   ", "555 ", "  5 ", "555 "],
    "6": ["666 ", "6   ", "666 ", "6 6 ", "666 "],
    "7": ["777 ", "  7 ", "  7 ", "  7 ", "  7 "],
    '8': ["888 ", "8 8 ", "888 ", "8 8 ", "888 "],
    "9": ["999 ", "9 9 ", "999 ", "  9 ", "999 "],
    ":": ["  ", ": ", "  ", ": ", "  "]
}