# Given an array of positive numbers and a positive number ‘S’, 
# find the length of the smallest contiguous subarray 
# whose sum is greater than or equal to ‘S’. 
# Return 0, if no such subarray exists.


def smallest_subarray_with_given_sum(s, arr):
    if not arr or s <= 0:
        return 0
    
    start, end = 0, 0
    curr_sum = 0
    smallest_len = len(arr) + 1
    while end < len(arr):
        curr = arr[end]
        if curr >= s:
            return 1
        curr_sum += curr
        while start < end and curr_sum >= s:
            smallest_len = min(smallest_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1
        end += 1
    
    return smallest_len if smallest_len != len(arr) + 1 else 0