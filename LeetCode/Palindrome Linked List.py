#https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        newlist = []
        while p:
            newlist.append(p.val)
            p = p.next

        i = 0
        j = len(newlist) - 1
        while i < j:
            if newlist[i] != newlist[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
