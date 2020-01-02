# Given a string with lowercase letters only, if you are allowed to replace
# no more than ‘k’ letters with any letter, find the length of the longest
# substring having the same letters after replacement.


# first, I thought this is the same problem as the no.3 (find the longest
# substring with at most k distinct characters). But it's not. Why?
# cause for this problem, any character can repeat as much as it can as
# as it wouldn't break the rules.

# Since we are only interested in the longest valid substring, our sliding
# windows need not shrink, even if a window may cover an invalid substring.
# We either grow the window by appending one char on the right, or shift the
# whole window to the right by one. And we only grow the window when the count
# of the new char exceeds the historical max count (from a previous window
# that covers a valid substring).

# w e do not need the accurate max count of the current window;
# we only care if the max count exceeds the historical max count; and that can
# only happen because of the new char.


def length_of_longest_substring(s, k):
    if not s or k < 0:
        return 0

    start, end = 0, 0
    freq_map = [0 for _ in range(26)]
    res = 0
    longest_repeats = 0

    while end < len(s):
        curr = s[end]
        index = ord(curr) - ord('a')
        freq_map[index] += 1
        longest_repeats = max(longest_repeats, freq_map[index])
        if end - start + 1 - longest_repeats <= k:
            res = max(res, end - start + 1)
        else:
            freq_map[ord(s[start]) - ord('a')] -= 1
            start += 1
            longest_repeats -= 1
        end += 1

    return res


if __name__ == "__main__":
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))
    print(length_of_longest_substring("aaabcdeeeee", 3))
