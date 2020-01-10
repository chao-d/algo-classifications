# Given an array containing 0s, 1s and 2s, sort the array in-place. You should
# treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s
# to recreate the array.

# The flag of the Netherlands consists of three colors: red, white and blue;
# and since our input array also consists of three different numbers that is
# why it is called Dutch National Flag problem.


def dutch_flag_sort(nums):
    if not nums:
        return

    start, end, index = 0, len(nums) - 1, 0
    while index <= end:
        if nums[index] == 1:
            index += 1
        elif nums[index] == 0:
            nums[index], nums[start] = nums[start], 0
            start += 1
            index += 1
        else:
            nums[index], nums[end] = nums[end], 2
            end -= 1
