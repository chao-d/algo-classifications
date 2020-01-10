# Given an array with positive numbers and a target number, find all of its
# contiguous subarrays whose product is less than the target number.


# count the number of subarray instead of return all of them
def find_subarrays(nums, k):
    if k == 0:
        return 0

    curr = 1
    start, count = 0, 0
    for end in range(len(nums)):
        curr *= nums[end]
        while start <= end and curr >= k:
            curr //= nums[start]
            start += 1
        count += end - start + 1

    return count
