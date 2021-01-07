# Find the sum of all left leaves in a given binary tree.

# Example:

    # 3
   # / \
  # 9  20
    # /  \
   # 15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, i=0, totalSum = 0) -> int:

        if not root:
            return 0
        if root.left:
            i += 1
            totalSum = self.sumOfLeftLeaves(root.left, i, totalSum)

        if root.right and not(root.right.right == None and root.right.left == None):
            i += 1
            totalSum = self.sumOfLeftLeaves(root.right, i, totalSum)

        if root.left == None and root.right == None:
            if i == 0: return 0
            totalSum += root.val

        return totalSum
