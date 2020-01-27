# Given a binary tree and a number sequence, find if the sequence is present
# as a root-to-leaf path in the given tree.


def find_path(root, sequence):
    if not root and not sequence:
        return True

    def dfs(root, sequence, curr):
        if not root:
            return sequence == curr
        curr.append(root.val)
        left = dfs(root.left, sequence, curr)
        right = dfs(root.right, sequence, curr)
        curr.pop()
        return left or right

    return dfs(root, sequence, [])
