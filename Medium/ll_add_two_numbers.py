"""
We are given with two linked lists, each node of which represents a digit of a number
the digits are represented in the reverse order
problem: to add the two numbers (consisting of the digits)

Clarification questions:
- How big is N (number)?
- A value of a node is 0-9?
- How important is it to take care of the space complexity in this problem?
- Time complexity?
- I assume that N be 0, and the last elements of the lists are not 0 unless we have number 0
- Are the lists of the same size?
- Can I re-write one of the lists?

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0;
        res = ListNode(0)
        n = res
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next;
            if l2:
                carry += l2.val;
                l2 = l2.next;
            carry, val = divmod(carry, 10)
            n.next = ListNode(val)
            n = n.next
        return res.next;
