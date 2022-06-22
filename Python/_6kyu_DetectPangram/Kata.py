import string

def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in s.lower():
        alphabet = alphabet.replace(char, "")
    return len(alphabet) == 0