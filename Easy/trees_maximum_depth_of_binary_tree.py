""" 
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

Questions:
can it be empty?

Test cases:
[]
[1, 2]
[1, null, 2]
[1, null, null]

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
#     def traverse(self, root, depth):
#         # print(root.val, depth)
#         l, r = None, None
#         if not root.left and not root.right:
#             return depth + 1
#         if root.left:
#             l = self.traverse(root.left, depth) + 1
#         if root.right:
#             r = self.traverse(root.right, depth) + 1
#         if l:
#             if r:
#                 return max(l, r)
#             return l
#         return r
        
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0
#         depth = 0
#         return self.traverse(root, depth)
    def maxDepth(self, root):
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
        