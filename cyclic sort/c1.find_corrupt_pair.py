"""
We are given an unsorted array containing ‘n’ numbers taken from the range 1
to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due
to a data error, one of the numbers got duplicated which also resulted in one
number going missing. Find both these numbers.
"""


def find_corrupt_numbers(nums):
    res = [-1] * 2
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            res[0] = abs(num)
        else:
            nums[idx] *= -1

    for i in range(len(nums)):
        if nums[i] > 0:
            res[1] = i + 1
            break

    return res
