# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # a b X c d
        # 1 2 3 4 5
        s = 0
        node = head
        while node.next:
            node = node.next
            s += 1
        s = s - n + 1
        if s == 0:
            head = head.next
            return head
        node = head
        c = 0
        while node and c + 1 < s:
            if node.next:
                node = node.next
                c += 1
        if node.next:
            tmp = node.next
            if node.next.next:
                node.next = node.next.next
            else:
                node.next = None     
            del tmp
        return head



