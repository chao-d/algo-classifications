# Given an array of positive numbers and a positive number ‘k’,
# find the maximum sum of any contiguous subarray of size ‘k’.


# start moving after end - start + 1 == k
def max_sub_array_of_size_k(k, arr):
    if k <= 0 or not arr or len(arr) < k:
        return -1

    start, end = 0, 0
    curr_sum = 0
    max_sum = 0
    while end < len(arr):
        curr_sum += arr[end]
        if end >= k - 1:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= arr[start]
            start += 1
        end += 1
    return max_sum
