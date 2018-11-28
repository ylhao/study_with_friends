#https://leetcode.com/problems/balanced-binary-tree/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        if root == None:
            return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1



