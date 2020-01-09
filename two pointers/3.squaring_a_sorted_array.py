# Given a sorted array, create a new array containing squares of all the
# number of the input array in the sorted order.

def make_squares(arr):
    if not arr:
        return arr

    res = [0] * len(arr)
    start, end = 0, len(arr) - 1
    index = len(arr) - 1
    while start <= end:
        if abs(arr[start]) >= abs(arr[end]):
            res[index] = arr[start] * arr[start]
            start += 1
        elif abs(arr[start]) < abs(arr[end]):
            res[index] = arr[end] * arr[end]
            end -= 1
        index -= 1
    return res
