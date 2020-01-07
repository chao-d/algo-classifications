# Given an array of characters where each character represents a fruit tree,
# you are given two baskets and your goal is to put maximum number of fruits
# in each basket.
# The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree.
# You will pick one fruit from each tree until you cannot,
# i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.


# this is the same as problem 3 except this problem replaces k with 2
def fruits_into_baskets(fruits):
    if not fruits:
        return 0

    start, end = 0, 0
    freq_map = {}
    max_len = 0
    while end < len(fruits):
        curr = fruits[end]
        if curr not in freq_map:
            freq_map[curr] = 0
        freq_map[curr] += 1
        if len(freq_map) <= 2:
            max_len = max(max_len, end - start + 1)
        else:
            while start < end:
                freq_map[fruits[start]] -= 1
                if freq_map[fruits[start]] == 0:
                    del freq_map[fruits[start]]
                    start += 1
                    break
                start += 1
        end += 1
    return max_len
