def find_level_averages(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [float(root.val)]

    res = []
    queue = collections.deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        level_sum = 0
        for _ in range(level_size):
            curr = queue.popleft()
            level_sum += curr.val
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        res.append(level_sum / level_size)

    return res
