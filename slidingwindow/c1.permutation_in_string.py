# Given a string and a pattern, find out if the string
# contains any permutation of the pattern.


def find_permutation(s, p):
    if not s or not p or len(p) > len(s):
        return False

    freq_map = {}
    for ch in p:
        if ch not in freq_map:
            freq_map[ch] = 0
        freq_map[ch] += 1

    total = 0
    start, end = 0, 0
    while end < len(s):
        prev, curr = s[start], s[end]
        if curr in freq_map:
            freq_map[curr] -= 1
            if freq_map[curr] == 0:
                total += 1
        if end >= len(p) - 1:
            if total == len(freq_map):
                return True
            if prev in freq_map:
                if freq_map[prev] == 0:
                    total -= 1
                freq_map[prev] += 1
            start += 1
        end += 1

    return False


def find_permutation_by_sorting(s, p):
    if not s or not p or len(p) > len(s):
        return False

    p_arr = sorted(list(p))
    s_arr = list(s)

    for i in range(0, len(s) - len(p) + 1):
        curr = sorted(s_arr[i:i+len(p)])
        if curr == p_arr:
            return True

    return False


if __name__ == "__main__":
    assert find_permutation("oidbcaf", "abc")
    assert find_permutation("aaacb", "abc")
    assert find_permutation("bcdxabcdy", "bcdyabcdx")
    assert find_permutation("pppppppqp", "qp")
    assert find_permutation("odicf", "dc")
