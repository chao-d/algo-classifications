"""
We are given an array containing ‘n’ distinct numbers taken from the range 0
to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers,
find the missing number.
"""


def find_missing_number(nums):
    if not nums:
        return -1

    return ((1 + len(nums)) * len(nums) // 2) - sum(nums)
