#https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        newlist = []
        while p:
            newlist.insert(0, p.val)
            p = p.next

        p = head
        for i in newlist:
            p.val = i
            p = p.next
        return head
