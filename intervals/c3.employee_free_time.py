def find_employee_free_time(schedule):
    flatten_schedules = sorted([s for e in schedule for s in e], \
                                key=lambda itv: itv.start)

    if len(flatten_schedules) == 1:
        return flattedn_schedules[0]

    res = []
    prev = flatten_schedules[0]
    for i in range(1, len(flatten_schedules)):
        curr = flatten_schedules[i]
        if prev.end >= curr.start:
            prev.end = max(prev.end, curr.end)
        else:
            res.append(Interval(prev.end, curr.start))
            prev = curr

    return res
