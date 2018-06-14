"""
Percentile: 97.38%

Problem:
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Solution:
Change "pointers" as in merge sort algorithm.

Time Complexity = O(N+M)
Space complexity = O(1)


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # node1, node2 = l1, l2
        # head = ListNode(0)
        # node = head
        # while node1 and node2:
        #     if node1.val <= node2.val:
        #         tmp = node1.next # save tmp
        #         node.next = node1 # append
        #         node = node.next # increment
        #         node.next = None # clean up node
        #         node1 = tmp # use tmp
        #     else:
        #         tmp = node2.next
        #         node.next = node2
        #         node = node.next
        #         node.next = None
        #         node2 = tmp
        # if node1:
        #     node.next = node1
        # else:
        #     node.next = node2
        # return head.next
    
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if not l1:
#             return l2
#         if not l2:
#             return l1
        
#         if l1.val < l2.val:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l2.next, l1)
#             return l2
    def mergeTwoLists(self, a, b):
        if not a or b and a.val > b.val:
            a, b = b, a
        if a:
            a.next = self.mergeTwoLists(a.next, b)
        return a