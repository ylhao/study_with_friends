# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/?tdsourcetag=s_pctim_aiomsg

# 以下代码为示例代码：
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fastPointer = head
        slowPointer = head
        while fastPointer != None and fastPointer.next != None:
            fastPointer = fastPointer.next.next  # 快指针走两步
            slowPointer = slowPointer.next  # 慢指针走一步
            if fastPointer == slowPointer:
                return True
        return False