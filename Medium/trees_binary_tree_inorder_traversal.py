"""
Percentile: 88%

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Clarification Questions:
Space, Time complexity?
How big is N
How big is height of the tree
Is it balanced tree?
Can the tree be empty? If so, what should I return? I assume I need to return an empty list.

Test cases:
[0]
[]
[1 2 3 4 5 6 7] 

     1 
  2     3
4  5   6  7

recursive:
append all of the following to a list:
    return left
    return root
    return right
return the list

time complexity nlog(n), space complexity n (storage of size N)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        lst = []
        if root.left:
            lst.extend(self.inorderTraversal(root.left))
        lst.extend([root.val])
        if root.right:
            lst.extend(self.inorderTraversal(root.right))
        return lst
        
        
        
        