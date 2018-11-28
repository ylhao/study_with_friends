#https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        res = []

        if root:
            queue.append(root)

        while len(queue) != 0:
            res.append([])
            nodeTemp = queue[0]
            res.append([nodeTemp.val])

            if nodeTemp.left:
                queue.append(nodeTemp.left)
            if nodeTemp.right:
                queue.append(nodeTemp.right)
            queue.pop(0)

            res.reverse()
            return res


			
# 修改为以下代码

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        queue = []
        queue.append(root)
        while len(queue) != 0:
            res.append([node.val for node in queue])
            queueTemp = []
            for node in queue:
                if node.left:
                    queueTemp.append(node.left)
                if node.right:
                    queueTemp.append(node.right)
            queue = queueTemp
        res.reverse()
        return res           
            