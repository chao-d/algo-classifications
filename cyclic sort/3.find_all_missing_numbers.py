"""
We are given an unsorted array containing numbers taken from the range 1
to ‘n’. The array can have duplicates, which means some numbers will be
missing. Find all those missing numbers.
"""


def find_missing_numbers(nums):
    if not nums or len(nums) < 2:
        return []

    for num in nums:
        idx = abs(num) - 1
        nums[idx] = -abs(nums[idx])

    res = []
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)

    return res
