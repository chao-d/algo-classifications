"""
We are given an unsorted array containing ‘n+1’ numbers taken from the range
1 to ‘n’. The array has only one duplicate but it can be repeated multiple
times. Find that duplicate number without using any extra space. You are,
however, allowed to modify the input array.
"""


def find_duplicate(nums):
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            return abs(num)
        nums[idx] *= -1
    return -1
