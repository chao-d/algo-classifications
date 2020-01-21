def calculate_bitwise_complement(n):
    if n == 0:
        return 1
    res, pos = 0, 0
    while n > 0:
        if n & 1 == 0:
            res |= (1 << pos)
        n >>= 1
        pos += 1
    return res
