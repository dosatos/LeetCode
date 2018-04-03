class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        storage = {} # where I will save difference and position; space complexity O(N)
        for idx, num in enumerate(nums): # time complexity O(N)
            lookup_diff = target - num # looking for this difference
            if lookup_diff in storage:
                return [storage[lookup_diff], idx];
            else:
                storage[num] = idx
        return "Not found";