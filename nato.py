#!/usr/bin/python
import sys
import json


def main():
    mappings = get_letter_to_code_mappings()
    if sys.argv[-1] == '-a':
        return get_whole_nato_alphabet_string(mappings)

    letter = get_wanted_letter()
    return mappings.get(letter)


def get_whole_nato_alphabet_string(mappings):
    """Get a string that represents all the mappings in the NATO alphabet."""
    def tuple_to_string(letter_word_pair):
        """Convert a tuple to a mapping string."""
        letter, word = letter_word_pair
        return '{letter}: {word}'.format(letter=letter, word=word)

    items = mappings.items()
    sorted_items = sorted(mappings.items())
    return '\n'.join(map(tuple_to_string, sorted_items))


def get_letter_to_code_mappings():
    """NATO phonetic alphabet.

    See "International Code of Signals" (INTERCO), United States
    Edition, 1969 Edition (Revised 2003) available from National
    Geospatial-Intelligence Agency at http://www.nga.mil/

    """
    return {
        "a": "Alfa", "b": "Bravo", "c": "Charlie", "d": "Delta", "e": "Echo",
        "f": "Foxtrot", "g": "Golf", "h": "Hotel", "i": "India", "j":
        "Juliett", "k": "Kilo", "l": "Lima", "m": "Mike", "n": "November", "o":
        "Oscar", "p": "Papa", "q": "Quebec", "r": "Romeo", "s": "Sierra", "t":
        "Tango", "u": "Uniform", "v": "Victor", "w": "Whiskey", "x": "Xray",
        "y": "Yankee", "z": "Zulu", "0": "Zero", "1": "One", "2": "Two", "3":
        "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8":
        "Eight", "9": "Niner", "=": "Equals", "?": "Query", "/": "Slash", ",":
        "Comma", ".": "Stop", ":": "Colon", "'": "Apostrophe", "-": "Dash",
        "(": "Open", ")": "Close", "@": "At",
    }


def get_wanted_letter():
    return sys.argv[-1]


if __name__ == '__main__':
    print main()
