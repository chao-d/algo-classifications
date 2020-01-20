def tree_right_view(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [root]

    res = []
    queue = collections.deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        is_first = True
        for _ in range(level_size):
            curr = queue.popleft()
            if is_first:
                res.append(curr)
                is_first = False
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)

    return res
