"""
We are given an array containing ‘n’ objects. Each object, when created, was
assigned a unique number from 1 to ‘n’ based on their creation sequence. This
means that the object with sequence number ‘3’ was created just before the
object with sequence number ‘4’.

Write a function to sort the objects in-place on their creation sequence
number in O(n)O(n) and without any extra space. For simplicity, let’s assume
we are passed an integer array containing only the sequence numbers, though
each number is actually an object.
"""


def cyclic_sort(nums):
    if nums is None or len(nums) < 2:
        return nums

    n = len(nums)
    for i in range(1, n + 1):
        nums[i - 1] = i
    return nums


if __name__ == "__main__":
    print(cyclic_sort([3, 1, 2, 5, 4, 6]))
