"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

Clarification questions:
How big is N?

Solution:
The easiest solution would be to use a dictionary:
- add to the dict each value seen with a value of 1
- and set the value to zero if the integer was seen twice
- after looping once, find a value with a value of 1
"""
import collections
    
class Solution:
    
    def singleNumber(self, nums):
        """
        using XOR operator
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res
    
#     def singleNumber(self, nums):
#         """
#         using Counter instead
#         :type nums: List[int]
#         :rtype: int
#         """
#         # use a container to look up value at a constant cost
#         # worst complexity O(N)
#         container = collections.Counter(nums)
        
#         # find the value that was seen only once
#         # worst complexity O((N-1)/2 + 1) => O(N) if N is very large
        
#         for k, v in container.items():
#             if v == 1:
#                 return k # Total complexity is O(N) in the worst case
#         return 0 # in case the list is empty
        
        
        
        
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # use a container to look up value at a constant cost
#         # worst complexity O(N)
#         container = {}
#         for num in nums:
#             try: # increase by one if seen already
#                 container[num] += 1
#             except: # add the number to the container otherwise
#                 container[num] = 0
        
#         # find the value that was seen only once
#         # worst complexity O((N-1)/2 + 1) => O(N) if N is very large
#         for k, v in container.items():
#             if v == 0:
#                 return k
#         return 0
        
#         # total complexity is O(N)
        