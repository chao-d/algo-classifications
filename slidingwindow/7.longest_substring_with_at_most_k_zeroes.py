# Given an array containing 0s and 1s, if you are allowed to replace no more
# than k 0s with 1s, find the length of the longest subarray having all 1s

# the problem is equivalent to "Find the longest subarray with at most k 0s"


def length_of_longest_substring(arr, k):
    if not arr or k < 0:
        return 0

    start, end = 0, 0
    num_of_zeroes = 0
    res = 0
    while end < len(arr):
        curr = arr[end]
        if curr == 1 or num_of_zeroes < k:
            if curr == 0:
                num_of_zeroes += 1
            res = max(res, end - start + 1)
            end += 1
        else:
            while start < end and arr[start] != 0:
                start += 1
            if start != end:
                start += 1
                num_of_zeroes -= 1
    return res


if __name__ == "__main__":
    assert length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
                                       3) == 9
    assert length_of_longest_substring([1, 1, 1, 0, 0, 1, 1, 1, 1],
                                       1) == 5
