"""
Some helpers I have come across to help with the Euler challenges
"""

# originally written for problem 8
def open_local_file(filename):
    """
    Open a file with the filename + extension in filename parameter
    """
    import os
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return open(os.path.join(__location__, filename), 'r')

INT_STRINGS_SIZES = {
    0: 0, #we don't say the zero 
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    100: 7,
    1000: 8
}