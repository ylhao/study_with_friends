# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/?tdsourcetag=s_pctim_aiomsg
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:  # 树不为空
            return self.helper(root.left, root.right)
        return True  # 树为空

    def helper(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.helper(p.right, q.left) and self.helper(p.left, q.right)
        return False
        