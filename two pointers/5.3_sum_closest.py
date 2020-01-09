# Given an array of unsorted numbers and a target number, find a triplet
# in the array whose sum is as close to the target number as possible, return
# the sum of the triplet. If there are more than one such triplet, return the
# sum of the triplet with the smallest sum.


def triplet_sum_close_to_target(arr, target_sum):
    if not arr or len(arr) < 3:
        return 0

    diff, res = float("inf"), float("inf")
    arr.sort()
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        j, k = i + 1, len(arr) - 1
        while j < k:
            while j != i + 1 and j < k and arr[j] == arr[j - 1]:
                j += 1
            while k != len(arr) - 1 and j < k and arr[k] == arr[k + 1]:
                k -= 1
            if j >= k:
                break
            curr = arr[i] + arr[j] + arr[k] - target_sum
            if curr == 0:
                return target_sum
            elif curr < 0:
                j += 1
            else:
                k -= 1
            if diff >= abs(curr):
                if diff == abs(curr):
                    if curr + target_sum < res:
                        res = curr + target_sum
                else:
                    res = curr + target_sum
                    diff = abs(curr)
    return res
