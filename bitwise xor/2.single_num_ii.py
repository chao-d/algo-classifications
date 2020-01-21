def singleNumber(self, nums: List[int]) -> int:
    res = 0
    for i in range(0, 32):
        count = 0
        for num in nums:
            count += (num >> i) & 1
        if count % 3 != 0:
            if i == 31:
                res += - 2 ** 31
            else:
                res |= 1 << i
    return res
