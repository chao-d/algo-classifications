# Given two strings containing backspaces (identified by the character ‘#’),
# check if the two strings are equal.


def backspace_compare(S, T):
    i = len(S) - 1
    j = len(T) - 1
    while True:
        back = 0
        while i >= 0 and (back > 0 or S[i] == "#"):
            back += 1 if S[i] == "#" else -1
            i -= 1
        while j >= 0 and (back > 0 or T[j] == "#"):
            back += 1 if T[j] == "#" else -1
            j -= 1
        if not (i >= 0 and j >= 0 and S[i] == T[j]):
            return i == -1 and j == -1
        i -= 1
        j -= 1
    return True
