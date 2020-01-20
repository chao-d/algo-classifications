def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    if len(intervals) == 1:
        return 1

    start, end = [], []
    for itv in intervals:
        start.append(itv.start)
        end.append(itv.end)
    start.sort()
    end.sort()

    count = 0
    i, j = 0, 0
    while i < len(start) and j < len(end):
        s = start[i]
        e = end[j]
        i += 1
        if s < e:
            count += 1
        else:
            j += 1
    return count
