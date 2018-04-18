'''
3Sum (Speed:95 percentile solution):
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Clarification Questions:
What should I return?
how important to handle memory complexity in this problem? what about time complexity?
how big is n? min/max values of n
how big elements of N are?
can elements of n be negative, zero, positive?
are the elements of N unique?

Test cases:
-1 0 1
3 2 -5
0 0 0
-1 0 1 3 2 -5 0 0 0

Approach:
n^3 matrix is one way of solving it. But the speed of the algorithm will be slow at large numbers.

since now duplicates I may take set of the values to get rid of the N.

if I store the values in a dictionary, then requesting the items will be quicker, but then I sacrifice the memory efficiency.

another approach is to sort from low to high

find a middle number and use to pointers starting from the edges and looking for a particular number in between (to come to 0).
gradually changing the pointers positions to the center one after another.

for ex -1 0 1 3 2 -5 0 0 0 -> set -> sort

=== -5 -1 0 1 2 3 ===
-5 3
-1 3
0 3 are pointless to check

-5 2
-1 2

-5 + 3 = 2 -> ok
-5 + 2 = 3 -> not found in between
-1 + 3 = 2 -> ok
-1 + 2 = 1 -> ok

Time Complexity O(N^2) <- nlog(N) for sorting <- n^2 for looking
Space Complexity O(N) <- storage of occurances

Special cases:
3 zeros
all numbers are positive
all numbers are negative
empty list


'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ### creating hash map to ease querying for the lookup_values
        storage = {}
        for i in nums:
            if i in storage:
                storage[i] += 1
            else:
                storage[i] = 1
        
        ### appending if there are at least three zeros
        res = [] # a store with the results
        if 0 in storage:
            if storage[0] >= 3:
                res.append([0, 0, 0])
                
        ### looking for the triples other than 3-zeros
        nums = sorted(list(set(nums)))
        l = 0
        for i in range(len(nums)):
            r = len(nums) - 1 ### right pointer to start from the last element each time left pointer is changed
            if nums[l] >= 0: ### break the look if there are no negative values left
                break
            for j in range(len(nums)):
                lookup_value = -(nums[l] + nums[r])
                if (lookup_value == nums[l] and lookup_value in storage and storage[lookup_value] == 1) or (lookup_value == nums[r] and lookup_value in storage and storage[lookup_value] == 1):
                    r -= 1
                    continue    
                if nums[r] <= 0: ### break the look if there are no positive values left
                    break
                if lookup_value in storage:
                    if nums[l] <= lookup_value <= nums[r]:
                        res.append([nums[l], lookup_value, nums[r]])
                r -= 1
            l += 1
        return res
        
                
        
        
        
        
            
        
        
        