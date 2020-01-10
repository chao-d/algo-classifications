# Given an array, find the length of the smallest subarray in it which when
# sorted will sort the whole array.


def shortest_window_sort(nums):
    start, end = 0, -1
    min_val, max_val = float("inf"), float("-inf")

    for i in range(len(nums)):
        j = len(nums) - 1 - i
        max_val = max(max_val, nums[i])
        if nums[i] < max_val:
            end = i
        min_val = min(min_val, nums[j])
        if nums[j] > min_val:
            start = j

    return end - start + 1
