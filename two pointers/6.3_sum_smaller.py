# Given an array arr of unsorted numbers and a target sum, count all triplets
# in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three
# different indices. Write a function to return the count of such triplets.


def triplet_with_smaller_sum(arr, target):
    if not arr or len(arr) < 3:
        return 0

    res = 0
    arr.sort()
    for i in range(len(arr) - 2):
        j, k = i + 1, len(arr) - 1
        while j < k:
            curr = arr[i] + arr[j] + arr[k]
            if curr < target:
                res += k - j
                j += 1
            else:
                k -= 1
    return res
