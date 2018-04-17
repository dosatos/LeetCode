"""
Question:
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Clarification Questions:

- shall I be concerned about space complexity, time complexity?
- how big is n?
- can n be 0?
- if n == 0, is result == 0? ____>>> NO, it will be 1!

Approach:
sum previous two: i.e. climb(N) = climb(N-1) + climb(N-2)
special cases if n == 2, 1, or 0

"""
    
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        if n == 2:
            return 2
        one, two, res = 2, 1, 0
        for i in range(2, n):
            res = one + two
            two = one
            one = res
        return res 