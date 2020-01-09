# Given an array of sorted numbers, remove all duplicates from it.
# You should not use any extra space; after removing the duplicates
# in-place return the new length of the array.


def remove_duplicates(arr):
    if not arr:
        return 0
    if len(arr) < 2:
        return len(arr)

    start, end = 1, 1
    while end < len(arr):
        if arr[end] == arr[start - 1]:
            end += 1
        else:
            arr[start] = arr[end]
            start += 1
            end += 1
    return start
