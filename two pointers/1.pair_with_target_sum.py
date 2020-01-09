# Given an array of sorted numbers and a target sum, find a pair in the array
# whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair)
# such that they add up to the given target.


def pair_with_targetsum(arr, target_sum):
    res = [-1, -1]
    if not arr:
        return res

    start, end = 0, len(arr) - 1
    while start < end:
        curr = arr[start] + arr[end]
        if curr == target_sum:
            res[0], res[1] = start, end
            return res
        elif curr < target_sum:
            start += 1
        else:
            end -= 1
    return res
