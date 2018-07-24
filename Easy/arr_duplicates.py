"""
How big is N?
how big the inside numbers are?
Does it contain numbers only?
Can it be empty?

Special Cases:
[]
[1, 2, 3]
[1, 2, 1]

Solution:
- iterate over the items storing them in a dictionary, once there is an item saved, return True. In case there is nothing till the end, return false.
Cost:
- Time complexity: O(N) 
- Space complexity: O(N)


Solution2:
if len(set(nums)) == len(nums):
    return False
return True
Cost:
- Time complexity: O(N) to return Set, O(1) to return len
- Space complexity: O(N)
"""

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False
        return True
