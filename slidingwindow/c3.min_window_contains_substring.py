# Given a string and a pattern, find the smallest substring in the given
# string which has all the characters of the given pattern.


def find_substring(s, t):
    freq_map = [0] * 256
    for c in t:
        freq_map[ord(c)] += 1

    start, end = 0, 0
    count = 0
    res, min_len = "", len(s) + 1

    while end < len(s):
        index = ord(s[end])
        freq_map[index] -= 1
        if freq_map[index] >= 0:
            count += 1

        while start <= end and count == len(t):
            if min_len > end - start + 1:
                min_len = end - start + 1
                res = s[start: end + 1]
            index0 = ord(s[start])
            freq_map[index0] += 1
            if freq_map[index0] > 0:
                count -= 1
                start += 1
                break
            start += 1
        end += 1
    return res


if __name__ == "__main__":
    # print(find_substring("aaaabcedfg", "af"))
    # print(find_substring("aaaaaaaaaaaabbbbbcdd", "abcdd"))
    # print(find_substring("a", "a"))
    print(find_substring("cabwefgewcwaefgcf", "cae"))
