""" 
Question:
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

Solution:

Info collection:
First of all I would collect as much as possible infromation about this task
and analyze the constraints of the problem, if possible:
- how important is it to consider space or time complexities in this problem?
    - note: from the task it is given that we have enough of space in num1 to append num2
- how big nums1 and num2 are?
- how big len pf nums1 and nums2?
- can nums1 on nums2 be empty?
- to confirm, nums1 and num2 have only integers/numbers, and no other symbols?

Test:
Now I am ready to think of cases and special cases:
a. [1, 2, 3] [1, 2] 
b. [] []
c. [0, 0, 0] []
d. [] [1, 999]

Approach:
Since I need to adjsut nums1 and not create another 
concatenate nums1 and nums2
left pointer to the beginning of nums1, right pointer to len(nums1)
swap if nums1[left] > nums1[right] and increase left++ and right++, keep "right" will be less than m + n
else left++
until left!=right

For the special cases, I will do initial validation, i.e. if any of the 
arrays is empty.

This will give me a Time Complexity O(N), Space complexity is O(num2)??.

"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        
        left = 0 # initialising pointers
        right = len(nums1) if m != 0 else 0 # pointer2 will be equal to the length of nums1 as indexing starts with 0
        nums1.extend(nums2) # concatenating two arrays
        
        while left != right:
            if nums1[left] > nums1[right]:
                nums1[left], nums1[right] = nums1[right], nums1[left]
                # increment pointer of the smaller element
                left += 1
                right = min(m + n - 1, right + 1)
            else:
                # increment pointer of the smallest element
                left += 1
            print(nums1)
    
                
            
            
        