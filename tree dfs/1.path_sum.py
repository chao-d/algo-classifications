# Given a binary tree and a number ‘S’, find if the tree has a path from root
# -to-leaf such that the sum of all the node values of that path equals ‘S’.


def has_path(root, sum):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == sum

    left = has_path(root.left, sum - root.val)
    right = has_path(root.right, sum - root.val)
    return left or right
