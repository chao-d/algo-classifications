# Given a string and a pattern, find the smallest substring in the given
# string which has all the characters of the given pattern.


def find_substring(s, p):
    if not s or not p or len(p) > len(s):
        return ""

    # if p == s:
    #     return p

    freq_map = {}
    for ch in p:
        if ch not in freq_map:
            freq_map[ch] = 0
        freq_map[ch] += 1

    count = 0
    start, end = 0, 0
    min_len = len(s) + 1
    res = ""
    while end < len(s):
        curr = s[end]
        if curr not in freq_map:
            end += 1
            continue

        freq_map[curr] -= 1
        if freq_map[curr] == 0:
            count += 1
        if count == len(freq_map):
            while start <= end:
                prev = s[start]
                if prev in freq_map:
                    freq_map[prev] += 1
                    if freq_map[prev] == 1:
                        if min_len > end - start + 1:
                            min_len = end - start + 1
                            res = s[start: end + 1]
                        start += 1
                        count -= 1
                        break
                start += 1
        end += 1
    print(min_len)
    return res


if __name__ == "__main__":
    # print(find_substring("aaaabcedfg", "af"))
    # print(find_substring("aaaaaaaaaaaabbbbbcdd", "abcdd"))
    # print(find_substring("a", "a"))
    print(find_substring("cabwefgewcwaefgcf", "cae"))
