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

Solution 2:
Percentile: 76% <<< Slower, but more memory efficient

Find len
Reverse the second half of the LL
Check for palindrome the first half to the second (reversed) half

Time Comlpexity: O(n)
Space Comlpexity: O(1)

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def isPalindrome(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     node = head
    #     container = []
    #     while node:
    #         container.append(node.val)
    #         node = node.next
    #     if container == container[::-1]:
    #         return True
    #     return False
        
    def isPalindrome(self, head):
        """ 
        Time complexity = O(N)
        Space complexity = O(1)
        """
        node = head
        length = 0
        # count the len of the ll
        while node:
            node = node.next
            length += 1
        
        # initialise first half head
        first_head = head
        node = head
        # 0 1 2 3 4 5 (6 // 2 = 3)
        # 0 1 2 3 4 5 6 (7 // 2 = 3)
        for _ in range(length // 2):
            node = node.next
        
        # skip the middle if odd
        if length % 2 != 0:
            node = node.next
        
        # reverse the second half
        prev_node = None
        while node:
            node.next, prev_node, node = prev_node, node, node.next
        second_head = prev_node
            
        # compare the two halves
        for _ in range(length // 2):
            if first_head.val != second_head.val:
                return False
            first_head = first_head.next
            second_head = second_head.next
        return True