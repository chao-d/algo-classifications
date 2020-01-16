"""
Given an unsorted array containing numbers, find the smallest missing
positive number in it.
"""


def find_first_missing_positive(nums):
    if not nums:
        return 1

    # quick selection then negtive marking
    end = quick_select(nums)
    if end < 0:
        return 1
    # negative marking
    marking_seen(nums, end)
    for i in range(end + 1):
        if nums[i] > 0:
            return i + 1

    return end + 2


def quick_select(nums):
    start, end = 0, len(nums) - 1
    while start <= end:
        if nums[start] > 0:
            start += 1
        else:
            nums[start], nums[end] = nums[end], nums[start]
            end -= 1
    return end


def marking_seen(nums, end):
    for i in range(end + 1):
        idx = abs(nums[i]) - 1
        if idx > end or nums[idx] < 0:
            continue
        nums[idx] *= -1
