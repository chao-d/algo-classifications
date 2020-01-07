# Given a string, find the length of the longest
# substring in it with no more than K distinct characters.


# keep moving end until the sliding window becomes invalid
# then move start to make it valid again
def longest_substring_with_k_distinct_ascii(s, k):
    if k <= 0 or not s:
        return 0

    start, end = 0, 0
    freq_map = [0] * 256
    count = 0
    longest_len = 0
    while end < len(s):
        curr = s[end]
        if freq_map[ord(curr)] == 0:
            count += 1
        freq_map[ord(curr)] += 1

        if count <= k:
            longest_len = max(longest_len, end - start + 1)
        else:
            while start <= end:
                freq_map[ord(s[start])] -= 1
                if freq_map[ord(s[start])] == 0:
                    count -= 1
                    start += 1
                    break
                start += 1
        end += 1
    return longest_len


def longest_substring_with_k_distinct(s, k):
    if k <= 0 or not s:
        return 0

    start, end = 0, 0
    freq_map = {}
    longest_len = 0
    while end < len(s):
        curr = s[end]
        if curr not in freq_map:
            freq_map[curr] = 0
        freq_map[curr] += 1

        if len(freq_map) <= k:
            longest_len = max(longest_len, end - start + 1)
        else:
            while start <= end:
                freq_map[s[start]] -= 1
                if freq_map[s[start]] == 0:
                    del freq_map[s[start]]
                    start += 1
                    break
                start += 1
        end += 1

    return longest_len
