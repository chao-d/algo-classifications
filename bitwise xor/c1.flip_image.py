def flip_and_invert_image(A):
    for row in A:
        i, j = 0, len(row) - 1
        while i < j:
            row[i], row[j] = row[j], row[i]
            row[i] ^= 1
            row[j] ^= 1
            i += 1
            j -= 1
        if i == j:
            row[i] ^= 1
    return A
