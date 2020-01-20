def connect_level_order_siblings(root):
    if not root or (not root.left and not root.right):
        return root

    queue = collections.deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        prev = None
        for _ in range(level_size):
            curr = queue.popleft()
            if not prev:
                prev = curr
            else:
                prev.next = curr
                prev = curr
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    return root
