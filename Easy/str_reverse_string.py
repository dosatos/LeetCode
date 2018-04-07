""" 
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

 Contraints related questions: 
 - how big is s?
 - how important space or time complexities in this case?
 - can s be empty?
"""

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        return s[::-1]