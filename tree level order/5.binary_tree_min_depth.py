def find_minimum_depth(root):
    if not root:
        return 0

    queue = collections.deque()
    queue.append(root)
    depth = 0
    while queue:
        level_size = len(queue)
        depth += 1
        for _ in range(level_size):
            curr = queue.popleft()
            if not curr.left and not curr.right:
                return depth
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    return 0
