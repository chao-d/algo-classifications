def find_successor(root, key):
    if not root or (not root.left and not root.right):
        return None

    res = None
    queue = collections.deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            curr = queue.popleft()
            if res and res.val == key:
                return curr
            res = curr
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    return None
