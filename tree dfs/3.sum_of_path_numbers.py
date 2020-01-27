# Given a binary tree where each node can only have a digit (0-9) value,
# each root-to-leaf path will represent a number. Find the total sum of all
# the numbers represented by all paths.


def find_sum_of_path_numbers(root):
    if not root:
        return 0

    def dfs(root, value, res):
        if not root:
            return

        if not root.left and not root.right:
            res.append(10 * value + root.val)
            return
        if root.left:
            dfs(root.left, 10 * value + root.val, res)
        if root.right:
            dfs(root.right, 10 * value + root.val, res)

    res = []
    dfs(root, 0, res)
    return sum(res)
