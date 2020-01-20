def find_tree_boundary(root):
    if not root:
        return []
    res = [root]
    if not root.left and not root.right:
        return res

    lefts, rights, leaves = [], [], []
    queue = deque()
    queue.append(root)
    while queue:
        size = len(queue)
        for i in range(size):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

            if curr == root:
                continue
            if i == 0:
                lefts.append(curr)
            elif not curr.left and not curr.right:
                leaves.append(curr)
            elif i == size - 1:
                rights.append(curr)

    rights.reverse()
    return res + lefts + leaves + rights
