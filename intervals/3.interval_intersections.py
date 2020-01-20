def merge(A, B):
    res = []
    if not A or not B:
        return res

    i, j = 0, 0
    while i < len(A) and j < len(B):
        currA = A[i]
        currB = B[j]
        if currA[1] < currB[0]:
            i += 1
        elif currA[0] > currB[1]:
            j += 1
        else:
            if currA[1] < currB[1]:
                i += 1
            else:
                j += 1
            res.append([max(currA[0], currB[0]), min(currA[1], currB[1])])

    return res
