def traverse(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [[root.val]]

    res = []
    deque = collections.deque()
    deque.append(root)
    is_even = True
    while deque:
        level_size = len(deque)
        curr_level = []
        for _ in range(level_size):
            if is_even:
                curr = deque.popleft()
                if curr.left:
                    deque.append(curr.left)
                if curr.right:
                    deque.append(curr.right)
            else:
                curr = deque.pop()
                if curr.right:
                    deque.appendleft(curr.right)
                if curr.left:
                    deque.appendleft(curr.left)
            curr_level.append(curr.val)
        is_even = not is_even
        res.append(curr_level)

    return res
