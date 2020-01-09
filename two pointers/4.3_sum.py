# Given an array of unsorted numbers, find all unique triplets
# in it that add up to zero.

def search_triplets(arr):
    if not arr or len(arr) < 3:
        return []

    res = []
    arr.sort()
    for i in range(len(arr) - 2):
        j, k = i + 1, len(arr) - 1
        while j < k:
            while j != i + 1 and j < k and arr[j] == arr[j - 1]:
                j += 1
            while k != len(arr) - 1 and j < k and arr[k] == arr[k + 1]:
                k -= 1
            if j >= k:
                break
            curr = arr[i] + arr[j] + arr[k]
            if curr == 0:
                res.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1
            elif curr < 0:
                j += 1
            else:
                k -= 1
    return res
