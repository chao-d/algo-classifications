# Given a binary tree and a number ‘S’, find all paths in the tree such that
# the sum of all the node values of each path equals ‘S’. Please note that the
# paths can start or end at any node but all paths must follow direction from
# parent to child (top to bottom).


def count_paths(root, S):
    count = [0]

    def dfs(root, tar, count, curr):
        if not root:
            return

        if tar == curr + root.val:
            count[0] += 1

        dfs(root.left, tar, count, curr)
        dfs(root.right, tar, count, curr)
        dfs(root.left, tar, count, curr + root.val)
        dfs(root.right, tar, count, curr + root.val)

    dfs(root, S, count, 0)
    return count[0]
