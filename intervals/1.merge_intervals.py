def merge(intervals):
    if not intervals:
        return []

    res = []
    intervals.sort(key=lambda itv: itv.start)
    for itv in intervals:
        if res and res[-1].end >= itv.start:
            res[-1].end = max(res[-1].end, itv.end)
        else:
            res.append(itv)

    return res
