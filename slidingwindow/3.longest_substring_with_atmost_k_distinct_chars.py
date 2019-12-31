# Given a string, find the length of the longest 
# substring in it with no more than K distinct characters.

def longest_substring_with_k_distinct(string, k):
    if k <= 0 or not string:
        return -1

    largest_index = dict()
    start, end = 0, 0
    count = 0
    len_substring = 0
    while end < len(string):
        curr = string[end]
        if curr in largest_index or count < k:
            len_substring = max(len_substring, end - start + 1)
            if curr not in largest_index:
                count += 1
                largest_index[curr] = 0
            largest_index[curr] += 1
            end += 1
        else:
            while start < end:
                largest_index[string[start]] -= 1
                if largest_index[string[start]] == 0:
                    del largest_index[string[start]]
                    count -= 1
                start += 1
                if count < k:
                    break

    return len_substring