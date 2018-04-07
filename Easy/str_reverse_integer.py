""" 
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 
32-bit signed integer range. For the purpose of this problem, assume that your function 
returns 0 when the reversed integer overflows.

Constarint related questions:
 - how big is X
 - can X be negative?
 - can X be empty
 - is this case memory/time complexity sensitive?
Solution:
    save the sign in coeff
    take abs value
    convert to string
    reverse
    convert back
    multiply by coeff
 
"""
import sys

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if isinstance(x, int):
            if x == 0:
                return 0
            sign = 1 if x >= 0 else -1
            x = int("".join(reversed(str(abs(x))))) * sign
            if x < -0x80000000 or x > 0x7fffffff:
                return 0
            return x
        else:
            return "Wrong Input"