# Find the path with the maximum sum in a given binary tree. Write a function
# that returns the maximum sum. A path can be defined as a sequence of nodes
# between any two nodes and doesn’t necessarily pass through the root.


def find_maximum_path_sum(root):
    if not root:
        return 0

    max_sum = [root.val]

    def max_path(root):
        if not root:
            return 0
        left = max(max_path(root.left), 0)
        right = max(max_path(root.right), 0)
        max_sum[0] = max(max_sum[0], left + right + root.val)
        return root.val + max(left, right)

    max_path(root)
    return max_sum[0]
