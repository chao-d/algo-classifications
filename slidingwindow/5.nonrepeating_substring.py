# Given a string, find the length of the longest
# substring which has no repeating characters.


def non_repeat_substring(s):
    if not s:
        return 0

    start, end = 0, 0
    index_map = {}
    longest_len = 0
    while end < len(s):
        curr = s[end]
        if curr not in index_map or index_map[curr] < start:
            longest_len = max(longest_len, end - start + 1)
        else:
            start = index_map[curr] + 1
        index_map[curr] = end
        end += 1
    return longest_len
