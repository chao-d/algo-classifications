"""
We are given an unsorted array containing ‘n’ numbers taken from the range 1
to ‘n’. The array has some duplicates, find all the duplicate numbers without
using any extra space.
"""


def find_all_duplicates(nums):
    res = []
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            res.append(abs(num))
            continue
        nums[idx] *= -1
    return res
