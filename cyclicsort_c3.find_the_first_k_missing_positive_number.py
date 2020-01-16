"""
Given an unsorted array containing numbers and a number ‘k’, find the first
‘k’ missing positive numbers in the array.
"""


def find_first_k_missing_positive(nums, k):
    res = []
    if not nums:
        for i in range(1, k + 1):
            res.append(i)
        return res

    # quick selection then negtive marking
    end = quick_select(nums)
    if end < 0:
        for i in range(1, k + 1):
            res.append(i)
        return res
    print("before", nums, end)
    # negative marking
    marking_seen(nums, end)
    seen = set()
    print("after", nums)
    for i in range(0, end + 1):
        if nums[i] > 0:
            res.append(i + 1)

    k -= len(res)
    curr = len(nums) + 1
    while k > 0:
        if curr not in seen:
            res.append(curr)
            k -= 1
        curr += 1

    return res


def quick_select(nums):
    start, end = 0, len(nums) - 1
    while start <= end:
        if nums[start] > 0:
            start += 1
        else:
            nums[start], nums[end] = nums[end], nums[start]
            end -= 1
    return end


def marking_seen(nums, end):
    for i in range(end + 1):
        idx = abs(nums[i]) - 1
        if idx > end or nums[idx] < 0:
            continue
        nums[idx] *= -1


if __name__ == "__main__":
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
