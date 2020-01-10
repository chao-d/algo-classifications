# Given an array of unsorted numbers and a target number, find all unique
# quadruplets in it, whose sum is equal to the target number.


def search_quadruplets(nums, target):
    if not nums or len(nums) < 4:
        return []

    nums.sort()
    res = []
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        three_sum(nums, target - nums[i], i, res)
    return res


def three_sum(nums, target, start, res):
    for i in range(start + 1, len(nums) - 2):
        if i != start + 1 and nums[i] == nums[i - 1]:
            continue
        j, k = i + 1, len(nums) - 1
        while j < k:
            while j != i + 1 and j < k and nums[j] == nums[j - 1]:
                j += 1
            while k != len(nums) - 1 and j < k and nums[k] == nums[k + 1]:
                k -= 1
            if j >= k:
                break
            curr = nums[i] + nums[j] + nums[k]
            if curr == target:
                res.append([nums[start], nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            elif curr < target:
                j += 1
            else:
                k -= 1
