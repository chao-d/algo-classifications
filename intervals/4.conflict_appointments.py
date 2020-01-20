def can_attend_all_appointments(intervals):
    if not intervals or len(intervals) < 2:
        return True
    intervals.sort(key=lambda itv: itv[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True
