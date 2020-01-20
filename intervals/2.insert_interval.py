def insert(intervals, new_interval):
    if not intervals or not intervals[0]:
        return [new_interval]

    intervals.sort(key=lambda itv: itv[0])
    start, end = -1, -1
    for i in range(len(intervals)):
        j = len(intervals) - 1 - i
        if intervals[j][1] >= new_interval[0]:
            start = j
        if intervals[i][0] <= new_interval[1]:
            end = i

    if start == -1:
        intervals.append(new_interval)
        return intervals
    if end == -1:
        intervals.insert(0, new_interval)
        return intervals

    merged_part = [min(new_interval[0], intervals[start][0]),
                   max(new_interval[1], intervals[end][1])]

    return intervals[:start] + [merged_part] + intervals[end + 1:]
