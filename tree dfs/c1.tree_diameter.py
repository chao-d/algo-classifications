# Given a binary tree, find the length of its diameter. The diameter of a tree
# is the number of nodes on the longest path between any two leaf nodes. The
# diameter of a tree may or may not pass through the root.


def find_diameter(self, root):
    if not root:
        return 0

    self.longest_sum = 0

    def lonegest_down(root):
        if not root:
            return 0
        left = lonegest_down(root.left)
        right = lonegest_down(root.right)
        self.longest_sum = max(self.longest_sum, left + right + 1)
        return 1 + max(left, right)

    lonegest_down(root)
    return self.longest_sum
