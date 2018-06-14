"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively 
or recursively. Could you implement both?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
    	return str(self.val)

class LL:
	def __init__(self, head):
		self.head = head
		self.idx = 0

	def reverseList_recursive(self):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		prev =  None
		curr = self.head  # A
		while curr:
			tmpNext = curr.next
			curr.next = prev
			prev = curr
			curr = tmpNext
		self.head = prev

	def reverseList_iterative(self):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		# A B C D
		stack = []
		node = self.head
		while node:
			stack.append(node)
			node = node.next
		
		preHead = ListNode(0)
		curr = preHead
		while stack:
			curr.next = stack.pop()
			curr = curr.next
		curr.next = None

		self.head = preHead.next

	def __str__(self):
		node = self.head
		container = []
		while node:
			container.append(node.val)
			node = node.next
		return ", ".join(map(str, container))


nodes = [ListNode(1), 
         ListNode(2), 
         ListNode(3), 
         ListNode(4), 
         ListNode(5)]


head = nodes[0]
for i, n in enumerate(nodes[:-1]):
	nodes[i].next = nodes[i+1]

lst = LL(head)
print("Original ", lst)
lst.reverseList_recursive()
print("Recursive", lst)

lst.reverseList_iterative()
print("Iterative", lst)
