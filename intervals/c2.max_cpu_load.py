import heapq


def find_max_cpu_load(jobs):
    jobs.sort(key=lambda job: job.start)
    heap = []
    curr_max = 0
    for job in jobs:
        curr_max = max(curr_max, job.cpu_load)
        while heap and heap[0][0] <= job.start:
            heapq.heappop(heap)
        if not heap:
            heapq.heappush(heap, (job.end, job.start, job.cpu_load))
        else:
            top = heapq.heappop(heap)
            end0, end1 = min(job.end, top[0]), max(job.end, top[0])
            job0 = (end0, job.start, top[2] + job.cpu_load)
            job1 = (end1, end0, top[2] if top[0] > job.end else job.cpu_load)
            heapq.heappush(heap, job0)
            heapq.heappush(heap, job1)
            curr_max = max(curr_max, job0[2])

    return curr_max
