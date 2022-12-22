import os

# clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# convert a column letter (e.g. A, B, C) to a number
def get_column(code):
    val = 0
    for ch in code:
        val = val * 26 + ord(ch) - ord("A") + 1
    return val - 1