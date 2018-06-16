"""
Percentile: 96.7%
Problem:
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

Solution:
The easiest solution would be to store all the values in a normal list
to check for polyndrome
Time Comlpexity: O(n)
Space Comlpexity: O(n)

"""
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
        node = head
        container = []
        while node:
            container.append(node.val)
            node = node.next
        if container == container[::-1]:
            return True
        return False