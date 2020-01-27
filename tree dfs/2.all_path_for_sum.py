# Given a binary tree and a number ‘S’, find all paths from root-to-leaf
# such that the sum of all the node values of each path equals ‘S’.


def find_paths(root, sum):
    if not root:
        return 0
    count = [0]
    def dfs(root, tar, count):
        if not root:
            return
        if not root.left and not root.right:
            if root.val == tar:
                count[0] += 1
            return

        dfs(root.left, tar - root.val, count)
        dfs(root.right, tar - root.val, count)

    dfs(root, sum, count)
    return count[0]
