import collections


def traverse(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [[root.val]]

    res = []
    queue = collections.deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        curr_level = []
        for _ in range(level_size):
            curr = queue.popleft()
            curr_level.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        res.append(curr_level)

    res.reverse()
    return res
